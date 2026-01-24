
import time
import hashlib
import json
import inspect

# --- In-Memory Cache ---
_cache = {}
_cache_expiry = {}
_DEFAULT_EXPIRATION = 3600  # 1 hour

def _get_cache_key(func, *args, **kwargs):
    """Creates a consistent, hashable key from function and arguments."""
    args_for_key = args
    # Use inspect to reliably determine if the function is a method.
    try:
        sig = inspect.signature(func)
        params = list(sig.parameters.keys())
        # If the function has parameters and the first one is 'self' or 'cls',
        # it's an instance or class method, so we exclude the first argument.
        if params and params[0] in ('self', 'cls'):
            args_for_key = args[1:]
    except (ValueError, TypeError):
        # Fallback for functions where signature cannot be determined.
        pass

    # Serialize arguments to a JSON string to handle dicts and other structures
    # Sorting the dict keys ensures that {'a': 1, 'b': 2} and {'b': 2, 'a': 1} produce the same key
    serialized_args = json.dumps((args_for_key, sorted(kwargs.items())), sort_keys=True)

    # Combine function name and serialized arguments
    raw_key = f"{func.__name__}:{serialized_args}"

    # Return a SHA256 hash for a consistent, fixed-length key
    return hashlib.sha256(raw_key.encode('utf-8')).hexdigest()

def cache_response(expiration_seconds=_DEFAULT_EXPIRATION):
    """
    A decorator to cache the results of a function in memory for a specified duration.

    This decorator is ideal for expensive, deterministic functions like API calls
    where you expect the same inputs to produce the same output.

    - Before execution, it checks if a valid (non-expired) cached result exists.
    - If a valid cache entry is found, it returns the cached data immediately.
    - If not, it executes the function, stores the result in the cache, and sets an expiration time.

    Args:
        expiration_seconds (int): The time in seconds for which the cache entry is valid.
                                  Defaults to 3600 seconds (1 hour).

    Returns:
        The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 1.  Meticulously craft a unique key for the function and its arguments
            # This ensures that `my_func('a')` and `my_func('b')` have different cache entries.
            key = _get_cache_key(func, *args, **kwargs)

            # 2. ⚡ Check for a FAST cache hit
            # If the result is in our cache and hasn't expired, we return it instantly.
            if key in _cache and time.time() < _cache_expiry[key]:
                print(f"⚡ Cache HIT for {func.__name__} with key: {key[:8]}...")
                return _cache[key]

            # 3. Cache MISS - Time to do the real work
            # If no valid cache entry is found, execute the original function.
            print(f"🐌 Cache MISS for {func.__name__} with key: {key[:8]}... Executing function.")
            result = func(*args, **kwargs)

            # 4. Store the new result and its expiration time in the cache
            # The next time this function is called with the same arguments, we'll have a cache hit.
            _cache[key] = result
            _cache_expiry[key] = time.time() + expiration_seconds

            return result
        return wrapper
    return decorator

def clear_cache():
    """Utility function to completely clear the in-memory cache."""
    global _cache, _cache_expiry
    _cache.clear()
    _cache_expiry.clear()
    print("🧹 Cache cleared.")

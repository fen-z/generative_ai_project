import time
import json
import threading
from functools import wraps

# --- In-Memory Cache ---
_cache = {}
_cache_expiry = {}
_cache_lock = threading.Lock()
_DEFAULT_EXPIRATION = 3600  # 1 hour
_sentinel = object()


def _get_cache_key(func_name, args, kwargs):
    """
    ⚡ Bolt Optimization: Fast & Robust Key Generation
    - Uses json.dumps with a fallback for non-serializable objects.
    - Sorting ensures consistent keys for same keyword arguments.
    """
    try:
        # default=str handles non-serializable objects like custom class instances
        serialized_args = json.dumps(
            (args, sorted(kwargs.items())), sort_keys=True, default=str
        )
    except Exception:
        # Ultimate fallback for cases where json.dumps totally fails
        serialized_args = str((args, sorted(kwargs.items())))

    return f"{func_name}:{serialized_args}"


def cache_response(expiration_seconds=_DEFAULT_EXPIRATION):
    """
    ⚡ Bolt Optimization: High-Performance Caching Decorator

    A decorator to cache the results of a function in memory for a specified duration.
    Optimized for speed, thread-safety, and robustness.

    - Uses fast string-based keys instead of redundant SHA256 hashing.
    - Thread-safe updates to the global cache.
    - Handles unhashable and non-serializable types (lists, dicts, custom objects).
    - Avoids expensive signature inspection on the hot path.

    Args:
        expiration_seconds (int): Time in seconds for which the cache entry is valid.
                                  Defaults to 1 hour.
    """

    def decorator(func):
        func_name = func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            # ⚡ Optimization: Fast key generation
            key = _get_cache_key(func_name, args, kwargs)
            now = time.time()

            # ⚡ Optimization: Combined existence check and retrieval
            # First check without lock for performance
            cached_val = _cache.get(key, _sentinel)
            if cached_val is not _sentinel:
                if now < _cache_expiry.get(key, 0):
                    return cached_val

            # Cache MISS
            result = func(*args, **kwargs)

            # Store result and expiration with thread safety
            with _cache_lock:
                _cache[key] = result
                _cache_expiry[key] = now + expiration_seconds

            return result

        return wrapper

    return decorator


def clear_cache():
    """Utility function to completely clear the in-memory cache."""
    with _cache_lock:
        _cache.clear()
        _cache_expiry.clear()

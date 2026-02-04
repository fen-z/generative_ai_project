import functools
import asyncio
import logging

logger = logging.getLogger(__name__)

def cached(func):
    """
    A decorator that caches the results of a function call.
    Supports both synchronous and asynchronous functions.
    Uses functools.lru_cache for high-performance in-memory caching.

    Note: Arguments to the cached function must be hashable.
    """
    if asyncio.iscoroutinefunction(func):
        @functools.lru_cache(maxsize=128)
        def _cached_wrapper(*args, **kwargs):
            # Cache the task to ensure the coroutine is only executed once
            # and subsequent calls await the same result.
            # Using asyncio.create_task (preferred for Python 3.7+)
            return asyncio.create_task(func(*args, **kwargs))

        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            return await _cached_wrapper(*args, **kwargs)
        return wrapper
    else:
        @functools.lru_cache(maxsize=128)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

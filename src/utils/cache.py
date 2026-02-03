import functools
import logging
from typing import Any, Callable

# Initialize logger for cache events
logger = logging.getLogger(__name__)


def cached(func: Callable) -> Callable:
    """
    ⚡ Bolt: High-performance caching decorator.

    Uses functools.lru_cache for extremely low-overhead in-memory caching.
    Ideal for reducing latency and costs associated with:
    - LLM API calls with identical prompts
    - Token counting for static text
    - Complex template formatting

    Default maxsize is 128, which provides a good balance between hit rate
    and memory usage for most generative AI applications.
    """

    @functools.lru_cache(maxsize=128)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Note: functools.lru_cache handles positional and keyword arguments
        # as of Python 3.8+, making it both fast and versatile.
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # We don't want to cache exceptions
            logger.error(f"Error in cached function {func.__name__}: {e}")
            raise

    # Add helper to clear cache if needed
    wrapper.clear_cache = wrapper.cache_clear

    return wrapper

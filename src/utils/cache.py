from functools import lru_cache
from typing import Callable, Union, overload


@overload
def cached(func: Callable) -> Callable: ...


@overload
def cached(*, maxsize: int = 128) -> Callable[[Callable], Callable]: ...


def cached(
    func: Union[Callable, None] = None, *, maxsize: int = 128
) -> Union[Callable, Callable[[Callable], Callable]]:
    """
    ⚡ Bolt Optimization: Optimized Caching Utility

    A decorator that caches the results of a function using an LRU (Least Recently Used) cache.
    This significantly improves performance for expensive operations like LLM API calls.

    Args:
        func: The function to be cached (optional if maxsize is provided).
        maxsize: Maximum size of the LRU cache (default: 128).
    """
    if func is None:
        return lru_cache(maxsize=maxsize)
    return lru_cache(maxsize=maxsize)(func)

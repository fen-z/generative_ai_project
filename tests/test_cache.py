import pytest
import time
from src.utils.cache import cached


def test_cached_basic():
    """Test that caching returns the same value and is faster."""
    call_count = 0

    @cached
    def increment(n):
        nonlocal call_count
        call_count += 1
        return n + 1

    # First call
    assert increment(5) == 6
    assert call_count == 1

    # Second call with same arg
    assert increment(5) == 6
    assert call_count == 1  # Should NOT increment call_count

    # Call with different arg
    assert increment(10) == 11
    assert call_count == 2


def test_cached_maxsize():
    """Test that maxsize is respected."""
    call_count = 0

    @cached(maxsize=2)
    def identity(n):
        nonlocal call_count
        call_count += 1
        return n

    identity(1)  # [1]
    identity(2)  # [1, 2]
    assert call_count == 2

    # In LRU, accessing an item makes it "most recent"
    # To evict 1, we should call 3 without re-accessing 1
    identity(3)  # [2, 3], 1 is evicted
    assert call_count == 3

    identity(1)  # cache miss
    assert call_count == 4


def test_cache_clear():
    """Test that cache_clear works."""
    call_count = 0

    @cached
    def get_val():
        nonlocal call_count
        call_count += 1
        return 42

    assert get_val() == 42
    assert call_count == 1

    assert get_val() == 42
    assert call_count == 1

    get_val.cache_clear()

    assert get_val() == 42
    assert call_count == 2


def test_cached_no_args():
    """Test using @cached without parentheses."""

    @cached
    def say_hello(name):
        return f"Hello {name}"

    assert say_hello("Bolt") == "Hello Bolt"
    assert say_hello("Bolt") == "Hello Bolt"


def test_cached_with_args():
    """Test using @cached with parentheses."""

    @cached(maxsize=10)
    def say_hi(name):
        return f"Hi {name}"

    assert say_hi("Bolt") == "Hi Bolt"
    assert say_hi("Bolt") == "Hi Bolt"

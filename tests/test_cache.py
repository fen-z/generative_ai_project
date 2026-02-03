import pytest
from src.utils.cache import cached
from src.utils.token_counter import count_tokens

def test_cache_functionality():
    call_count = 0

    @cached
    def increment(x):
        nonlocal call_count
        call_count += 1
        return x + 1

    assert increment(1) == 2
    assert call_count == 1
    assert increment(1) == 2
    assert call_count == 1
    assert increment(2) == 3
    assert call_count == 2

def test_token_counter_optimization():
    text = "Hello world"
    # First call
    count1 = count_tokens(text)
    # Second call (cached)
    count2 = count_tokens(text)

    assert count1 == count2
    assert count1 > 0

def test_cache_clear():
    # Test that we can clear the cache
    count_tokens.clear_cache()
    # This should still work
    assert count_tokens("test") > 0

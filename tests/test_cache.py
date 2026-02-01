import time
import pytest
from src.utils.cache import cache_response, clear_cache


def test_basic_caching():
    clear_cache()
    call_count = 0

    @cache_response(expiration_seconds=10)
    def add(a, b):
        nonlocal call_count
        call_count += 1
        return a + b

    assert add(1, 2) == 3
    assert call_count == 1
    assert add(1, 2) == 3
    assert call_count == 1  # Should be cached

    assert add(2, 3) == 5
    assert call_count == 2


def test_unhashable_args():
    clear_cache()
    call_count = 0

    @cache_response()
    def process_data(data):
        nonlocal call_count
        call_count += 1
        return len(data)

    data = {"messages": [{"role": "user", "content": "hello"}]}
    assert process_data(data) == 1
    assert call_count == 1
    assert process_data(data) == 1
    assert call_count == 1  # Should be cached despite being a dict


def test_non_serializable_args():
    clear_cache()
    call_count = 0

    class CustomObj:
        def __str__(self):
            return "custom"

    @cache_response()
    def process_custom(obj):
        nonlocal call_count
        call_count += 1
        return str(obj)

    obj = CustomObj()
    assert process_custom(obj) == "custom"
    assert call_count == 1
    assert process_custom(obj) == "custom"
    assert call_count == 1  # Should be cached!


def test_expiration():
    clear_cache()
    call_count = 0

    @cache_response(expiration_seconds=0.1)
    def get_time():
        nonlocal call_count
        call_count += 1
        return time.time()

    t1 = get_time()
    assert call_count == 1
    t2 = get_time()
    assert t1 == t2
    assert call_count == 1

    time.sleep(0.15)
    t3 = get_time()
    assert t3 > t1
    assert call_count == 2


def test_method_caching_per_instance():
    clear_cache()

    class Calculator:
        def __init__(self, name):
            self.name = name
            self.call_count = 0

        @cache_response()
        def multiply(self, a, b):
            self.call_count += 1
            return a * b

    calc1 = Calculator("calc1")
    assert calc1.multiply(2, 3) == 6
    assert calc1.call_count == 1
    assert calc1.multiply(2, 3) == 6
    assert calc1.call_count == 1

    calc2 = Calculator("calc2")
    assert calc2.multiply(2, 3) == 6
    # In the new implementation, calc2 has a different 'self', so it's a different key.
    # This is safer and prevents cross-instance contamination.
    assert calc2.call_count == 1


def test_clear_cache():
    clear_cache()
    call_count = 0

    @cache_response()
    def foo(x):
        nonlocal call_count
        call_count += 1
        return x

    foo(1)
    assert call_count == 1
    foo(1)
    assert call_count == 1

    clear_cache()
    foo(1)
    assert call_count == 2

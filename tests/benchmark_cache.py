import time
import asyncio
from src.utils.cache import cached
from src.utils.token_counter import count_tokens

def test_sync_cache_speed():
    text = "This is a long text that needs to be counted for tokens multiple times." * 100

    # First call (uncached)
    start_time = time.perf_counter()
    count1 = count_tokens(text)
    uncached_duration = time.perf_counter() - start_time

    # Second call (cached)
    start_time = time.perf_counter()
    count2 = count_tokens(text)
    cached_duration = time.perf_counter() - start_time

    assert count1 == count2
    print(f"\nSync Uncached duration: {uncached_duration:.6f}s")
    print(f"Sync Cached duration:   {cached_duration:.6f}s")
    print(f"Speedup: {uncached_duration / (cached_duration + 1e-9):.2f}x")

    assert cached_duration < uncached_duration

def test_async_cache_speed_runner():
    async def run_test():
        @cached
        async def slow_async_func(x):
            await asyncio.sleep(0.1)
            return x * 2

        # First call (uncached)
        start_time = time.perf_counter()
        res1 = await slow_async_func(10)
        uncached_duration = time.perf_counter() - start_time

        # Second call (cached)
        start_time = time.perf_counter()
        res2 = await slow_async_func(10)
        cached_duration = time.perf_counter() - start_time

        assert res1 == res2
        print(f"\nAsync Uncached duration: {uncached_duration:.6f}s")
        print(f"Async Cached duration:   {cached_duration:.6f}s")
        print(f"Speedup: {uncached_duration / (cached_duration + 1e-9):.2f}x")

        assert cached_duration < uncached_duration
        assert cached_duration < 0.05

    asyncio.run(run_test())

if __name__ == "__main__":
    test_sync_cache_speed()
    test_async_cache_speed_runner()

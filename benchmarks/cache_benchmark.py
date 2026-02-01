import time
import sys
import os
from src.utils.cache import cache_response, clear_cache

@cache_response()
def dummy_func(x):
    return x

def run_benchmark(iterations=10000):
    print(f"Running benchmark with {iterations} iterations...")

    # Suppress internal prints
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    start = time.time()
    for i in range(iterations):
        dummy_func(1)
    end = time.time()

    sys.stdout = original_stdout
    duration = end - start
    print(f"Time taken for {iterations} cached calls: {duration:.4f}s")
    print(f"Average time per call: {duration/iterations*1000000:.2f} µs")

if __name__ == "__main__":
    clear_cache()
    # First call to populate cache
    dummy_func(1)
    run_benchmark()

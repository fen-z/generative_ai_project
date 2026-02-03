import time
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.utils.token_counter import count_tokens

def run_benchmark():
    print("⚡ Bolt Token Counter Optimization Benchmark ⚡")

    text = "Generative AI is transforming the way we build software. " * 10
    iterations = 1000

    print(f"\nCounting tokens for a string of {len(text)} characters, {iterations} times.")

    # Run with cache
    start = time.time()
    for _ in range(iterations):
        count_tokens(text)
    end = time.time()
    cached_time = end - start
    print(f"Time with caching: {cached_time:.6f}s")

    # Run without cache (clearing it every time)
    start = time.time()
    for _ in range(iterations):
        count_tokens.clear_cache()
        count_tokens(text)
    end = time.time()
    uncached_time = end - start
    print(f"Time without caching (simulated): {uncached_time:.6f}s")

    improvement = (uncached_time - cached_time) / uncached_time * 100
    print(f"\n📊 Performance Improvement: {improvement:.2f}%")
    print(f"🚀 Speedup: {uncached_time / cached_time:.2f}x")

if __name__ == "__main__":
    run_benchmark()

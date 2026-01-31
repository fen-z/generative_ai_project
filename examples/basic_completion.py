import time
import sys
import os

# Add src to path to ensure we can import the utils
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.utils.cache import cached


@cached
def mock_llm_call(prompt: str) -> str:
    """
    Simulates a slow LLM API call.
    """
    time.sleep(1.5)  # Simulate network latency and processing time
    return f"Response for: {prompt}"


def run_benchmark():
    print("⚡ Bolt Performance Benchmark ⚡")
    print("-" * 30)

    prompt = "Explain the importance of caching in Generative AI."

    # First call - Cold cache
    print(f"1. First call (Cold cache): '{prompt}'")
    start_time = time.time()
    response1 = mock_llm_call(prompt)
    duration1 = time.time() - start_time
    print(f"Duration: {duration1:.4f}s")

    # Second call - Warm cache
    print(f"\n2. Second call (Warm cache): '{prompt}'")
    start_time = time.time()
    response2 = mock_llm_call(prompt)
    duration2 = time.time() - start_time
    print(f"Duration: {duration2:.4f}s")

    # Verification
    assert response1 == response2
    print("-" * 30)

    if duration2 < duration1:
        speedup = duration1 / duration2 if duration2 > 0 else float("inf")
        print(f"✅ Success! Cache hit is significantly faster.")
        print(f"Estimated Speedup: {speedup:,.2f}x")
        print(f"Time Saved: {duration1 - duration2:.4f}s")
    else:
        print("❌ Error: Caching did not improve performance.")


if __name__ == "__main__":
    run_benchmark()

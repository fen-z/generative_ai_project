import time
import sys
import os

# Add the project root to the Python path to allow importing from `src`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.cache import cached

# ⚡ Bolt's Caching Demonstration
#
# This script demonstrates the performance benefit of the @cached decorator.

# 1. Define an "expensive" function.
#    This function simulates a slow network request or a heavy computation.
#    The `@cached` decorator is applied to it.
@cached(maxsize=128)
def expensive_api_call(prompt: str) -> str:
    """
    Simulates a function that takes a long time to execute,
    like an API call to a generative AI model.
    """
    print(f"\n📞 Making a slow API call for: '{prompt}'... (This should only happen once per prompt)")
    time.sleep(2)  # Simulate 2-second network latency
    response = f"Response for '{prompt}'"
    print("✅ API call complete.")
    return response

def main():
    """
    Runs the demonstration.
    """
    print("--- Caching Decorator Performance Test ---")
    print("First call to expensive_api_call('Hello, Bolt!'):")
    start_time = time.time()
    result1 = expensive_api_call("Hello, Bolt!")
    end_time = time.time()
    print(f"📄 Result: {result1}")
    print(f"⏱️  Time taken: {end_time - start_time:.2f} seconds")

    print("\n" + "="*40 + "\n")

    print("Second call to expensive_api_call('Hello, Bolt!'):")
    print("(This time, the result should be returned instantly from the cache)")
    start_time = time.time()
    result2 = expensive_api_call("Hello, Bolt!")
    end_time = time.time()
    print(f"📄 Result: {result2}")
    print(f"⏱️  Time taken: {end_time - start_time:.4f} seconds")

    print("\n" + "="*40 + "\n")

    print("First call with a DIFFERENT prompt ('Cache Test'):")
    start_time = time.time()
    result3 = expensive_api_call("Cache Test")
    end_time = time.time()
    print(f"📄 Result: {result3}")
    print(f"⏱️  Time taken: {end_time - start_time:.2f} seconds")

    print("\n" + "="*40 + "\n")

    print("Verifying the cache works as expected...")
    assert result1 == result2, "Cache returned a different result for the same input!"
    print("✅ Verification successful: The cache provides consistent results.")

if __name__ == "__main__":
    main()

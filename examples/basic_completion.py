
import sys
import os
import time

# Add the project root to the Python path to allow for absolute imports
# This is necessary to run the script directly and have it find the `src` module.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llm.openai_client import OpenAIClient
from src.utils.cache import clear_cache

def measure_generation_time(client, prompt):
    """Helper function to call the generate method and measure its execution time."""
    start_time = time.time()
    response = client.generate(prompt)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Response: '{response}'")
    print(f"⏱️  Time taken: {duration:.2f} seconds")
    return duration

def main():
    """
    A script to demonstrate the functionality and performance benefit of the cache decorator.
    """
    print("--- ⚡ Bolt's Caching Performance Demonstration ---")
    print("This script showcases how caching avoids re-running expensive functions (like API calls).\n")

    # 1. Initialize the OpenAI client.
    # A dummy API key is sufficient for this simulation.
    openai_client = OpenAIClient(api_key="DUMMY_API_KEY_FOR_DEMO")

    # 2. Define a prompt that we will reuse.
    my_prompt = "What is the speed of light?"

    print("\n--- First API Call (EXPECTED CACHE MISS) ---")
    print("This first call will be slow, as it needs to execute the function and simulate the API delay.")
    first_call_duration = measure_generation_time(openai_client, my_prompt)

    print("\n--- Second API Call (EXPECTED CACHE HIT) ---")
    print("This second call with the *exact same prompt* should be nearly instantaneous.")
    second_call_duration = measure_generation_time(openai_client, my_prompt)

    # 3. Analyze and report the performance improvement.
    print("\n--- 📊 Performance Analysis ---")
    if second_call_duration < first_call_duration:
        # Calculate the percentage improvement.
        improvement = (first_call_duration - second_call_duration) / first_call_duration * 100
        print(f"✅ Success! The cached call was ~{improvement:.0f}% faster.")
        print("The result was served from the in-memory cache, skipping the simulated 2-second API delay.")
    else:
        print("❌ Anomaly Detected. The cached call was not faster, caching may not be working as expected.")

    # 4. Demonstrate that a different prompt results in another cache miss.
    print("\n--- Third API Call with a NEW Prompt (EXPECTED CACHE MISS) ---")
    print("This call uses a new prompt, so it will be slow again.")
    measure_generation_time(openai_client, "What is the capital of France?")

    # 5. Demonstrate the effect of clearing the cache.
    print("\n--- Clearing the Cache ---")
    clear_cache()
    print("\n--- Fourth API Call with Original Prompt (EXPECTED CACHE MISS) ---")
    print("Even though we've used this prompt before, the cache has been cleared, so it will be slow again.")
    measure_generation_time(openai_client, my_prompt)

if __name__ == "__main__":
    main()

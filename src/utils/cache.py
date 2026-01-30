from functools import lru_cache

# ⚡ Bolt's Optimization: High-Performance Caching
#
# 💡 What: This module implements a high-performance, in-memory cache using Python's
# built-in `lru_cache` from the `functools` library.
#
# 🎯 Why: Generative AI models often involve expensive, time-consuming API calls.
# Caching the results of these calls is a critical performance optimization. It
# avoids redundant computations and network latency for repeated requests with the
# same inputs, leading to significant speed improvements and reduced API costs.
#
# 📊 Impact:
#   - Latency Reduction: Subsequent calls with the same arguments will return
#     almost instantly, as the result is fetched from memory instead of being
#     recomputed or fetched over the network.
#   - Cost Savings: Reduces the number of API calls to paid services, lowering
#     operational costs.
#   - Improved User Experience: Faster response times lead to a more responsive
#     and satisfying user experience.
#
# 🔬 Measurement:
# To verify the improvement, you can time a function decorated with `@cached`
# on its first and second run with the same inputs. The second run should be
# orders of magnitude faster.
#
# Example Usage:
# from src.utils.cache import cached
#
# @cached(maxsize=128)
# def expensive_api_call(prompt):
#   # Simulate a network request
#   print(f"Making an expensive API call for: {prompt}")
#   time.sleep(2)
#   return f"Response for {prompt}"
#
# print(expensive_api_call("Hello"))  # Takes ~2 seconds
# print(expensive_api_call("Hello"))  # Returns instantly

# The `lru_cache` decorator is aliased as `cached` for clarity.
# It can be applied to any function to cache its return values.
cached = lru_cache

## 2025-01-31 - Optimized Decorator Pattern
**Learning:** Using a custom wrapper around `functools.lru_cache` adds unnecessary overhead. `lru_cache` already preserves function metadata and exposes cache management methods. Returning the result of `lru_cache` directly is more efficient.
**Action:** Use `lru_cache` directly or with a minimal dispatcher to handle both `@cached` and `@cached(maxsize=N)` patterns without adding an extra closure layer.

## 2025-01-31 - Cache Eviction Testing
**Learning:** When testing LRU (Least Recently Used) cache eviction, remember that accessing an item moves it to the "most recent" position. A naive sequence of calls might not evict the expected item if it was re-accessed during the test.
**Action:** Carefully plan the sequence of accesses to ensure the target item remains the least recently used before triggering eviction.

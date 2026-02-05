## 2025-02-04 - Repository Hygiene and Build Artifacts
**Learning:** Committing Python build artifacts like `__pycache__/` or `*.pyc` files leads to repository bloat and potential conflicts. Always use a `.gitignore` file to exclude these artifacts.
**Action:** Always ensure a `.gitignore` is present and correctly configured to exclude platform-specific and build-related files before submitting changes.

## 2025-02-04 - Modern Async Patterns
**Learning:** `asyncio.create_task` is the preferred way to schedule coroutines in modern Python (3.7+) over `asyncio.ensure_future`, providing better clarity and integration with the event loop.
**Action:** Use `asyncio.create_task` for scheduling tasks in async decorators and workflows.

## 2025-02-05 - Regex Pre-compilation and Internal Caching
**Learning:** While Python's `re` module internally caches compiled patterns, explicitly pre-compiling regex at the module level still provides a measurable performance boost by avoiding dictionary lookups and internal overhead in hot paths. It also ensures consistent performance regardless of other regex usage in the application which might evict patterns from the internal `re` cache.
**Action:** Pre-compile frequently used regular expressions at the module level.

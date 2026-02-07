## 2025-02-04 - Repository Hygiene and Build Artifacts
**Learning:** Committing Python build artifacts like `__pycache__/` or `*.pyc` files leads to repository bloat and potential conflicts. Always use a `.gitignore` file to exclude these artifacts.
**Action:** Always ensure a `.gitignore` is present and correctly configured to exclude platform-specific and build-related files before submitting changes.

## 2025-02-04 - Modern Async Patterns
**Learning:** `asyncio.create_task` is the preferred way to schedule coroutines in modern Python (3.7+) over `asyncio.ensure_future`, providing better clarity and integration with the event loop.
**Action:** Use `asyncio.create_task` for scheduling tasks in async decorators and workflows.

## 2025-02-06 - Regex Pre-compilation and Token Counting
**Learning:** In Python 3.12, pre-compiling a regex pattern with `re.compile()` provides a measurable 1.5x-1.7x speedup over passing the pattern string directly to `re.findall()`, even with Python's internal regex caching. For token counting, `len(re.findall())` is significantly faster (~1.2x) than `sum(1 for _ in re.finditer())` despite the list allocation.
**Action:** Always pre-compile regex patterns used in high-frequency functions or loops. Prefer `findall` over `finditer` when only the count is needed and memory for the list of tokens is not a bottleneck.

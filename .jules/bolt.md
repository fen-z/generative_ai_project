## 2025-02-04 - Repository Hygiene and Build Artifacts
**Learning:** Committing Python build artifacts like `__pycache__/` or `*.pyc` files leads to repository bloat and potential conflicts. Always use a `.gitignore` file to exclude these artifacts.
**Action:** Always ensure a `.gitignore` is present and correctly configured to exclude platform-specific and build-related files before submitting changes.

## 2025-02-04 - Modern Async Patterns
**Learning:** `asyncio.create_task` is the preferred way to schedule coroutines in modern Python (3.7+) over `asyncio.ensure_future`, providing better clarity and integration with the event loop.
**Action:** Use `asyncio.create_task` for scheduling tasks in async decorators and workflows.

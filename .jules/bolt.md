## 2025-02-03 - Caching in Skeleton Projects
**Learning:** When working with a skeleton project or template, the best performance impact comes from implementing core utilities with optimization-first patterns (like memoization) rather than just adding boilerplate.
**Action:** Always provide a benchmark when implementing a new optimized utility to prove its value.

## 2025-02-03 - Python Bytecode in PRs
**Learning:** Running tests and benchmarks in Python generates `__pycache__` directories which should never be committed.
**Action:** Always add a `.gitignore` and clean up bytecode before submitting.

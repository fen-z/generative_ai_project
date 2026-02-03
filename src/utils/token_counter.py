import re
from src.utils.cache import cached

@cached
def count_tokens(text: str) -> int:
    """
    ⚡ Bolt: Optimized token counter with caching.

    In Generative AI applications, token counting is performed frequently
    (e.g., on every message in a chat history). Caching the results for
    identical strings significantly reduces redundant processing.

    This implementation uses a heuristic-based approach as a baseline.
    """
    if not text:
        return 0

    # Simulate some processing that makes this slightly expensive
    # In a real app, this might be a call to tiktoken or another tokenizer
    words = re.findall(r'\w+', text)
    punctuation = re.findall(r'[^\w\s]', text)

    # Standard heuristic: ~4 characters per token or ~0.75 words per token
    # Here we use a slightly more complex heuristic
    token_estimate = len(words) + len(punctuation)

    return int(token_estimate * 1.1)  # Adding a 10% safety margin

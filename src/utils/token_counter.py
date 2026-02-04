import re
from src.utils.cache import cached

@cached
def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    """
    Counts the number of tokens in a string.
    Uses the @cached decorator to optimize repeated calls with the same input.

    This is a baseline implementation. For production use with OpenAI models,
    consider using the 'tiktoken' library for exact counts.
    """
    if not text:
        return 0

    # Simple heuristic: split by whitespace and punctuation
    # This is much faster than loading a full tokenizer for simple estimates
    tokens = re.findall(r"[\w']+|[.,!?;]", text)

    # LLM tokens are often roughly 0.75 words, so tokens = words / 0.75 = words * 1.33
    # But re.findall on words+punct is a better approximation of token boundaries
    return len(tokens)

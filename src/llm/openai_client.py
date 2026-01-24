
import time
from src.llm.base import BaseLLMClient
from src.utils.cache import cache_response

class OpenAIClient(BaseLLMClient):
    """
    A concrete implementation of the LLM client for OpenAI's API.

    This class simulates making an API call to an OpenAI model.
    The `generate` method is intentionally slow to demonstrate the
    performance benefit of caching.
    """

    def __init__(self, api_key: str, model: str = "gpt-4"):
        """
        Initializes the OpenAI client.

        Args:
            api_key (str): The API key for the OpenAI service.
            model (str): The model name to use for generation.
        """
        self.api_key = api_key
        self.model = model
        print(f"OpenAIClient initialized with model: {self.model}")

    @cache_response(expiration_seconds=60)
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generates a response using a simulated OpenAI API call.

        - This method is decorated with `@cache_response`, so the first call
          with a specific prompt will be slow, but subsequent identical calls
          (within the 60-second cache window) will return instantly.
        - A 2-second delay is added to simulate network latency and model
          inference time.

        Args:
            prompt (str): The input prompt for the model.
            **kwargs: Additional parameters like 'temperature' or 'max_tokens'.

        Returns:
            str: A simulated response from the language model.
        """
        print(f"\n>> Simulating an expensive API call to OpenAI for prompt: '{prompt[:30]}...'")

        # Simulate the time it takes to get a response from an actual API
        time.sleep(2)

        # In a real implementation, this is where the actual API call would be.
        # For this example, we'll just return a formatted string.
        response = f"This is a simulated response for the prompt: '{prompt}' using model {self.model}."

        print("<< OpenAI API call simulation finished.")
        return response

    def get_provider_name(self) -> str:
        """Returns the specific provider name."""
        return "OpenAI"

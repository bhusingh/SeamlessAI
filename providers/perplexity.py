"""
Simulated Perplexity adapter for MVP.

Because Perplexity may not provide a public API in your environment, this adapter
simulates another provider by re-prompting OpenAI with a different system prompt
and temperature. Replace this with a real Perplexity adapter if/when you have an API.
"""

from providers.openai import OpenAIProvider

class PerplexityProvider(OpenAIProvider):
    def __init__(self):
        # create a "different" OpenAI provider config to simulate another provider
        super().__init__(model="gpt-4o", temperature=0.8)

    def name(self):
        return "Perplexity-simulated"

    def query(self, prompt):
        # Add a provider-specific prefix to emulate different style/source
        enhanced_prompt = (
            "You are Perplexity-simulated: aim for concise direct answers, show sources where appropriate.\n\n"
            + prompt
        )
        return super().query(enhanced_prompt)

"""
Aggregation utilities.
- concatenate: simple concat with labels
- meta_summarize: ask OpenAI to synthesize a single coherent answer from provider outputs + context
"""

from providers.openai_provider import OpenAIProvider

class Aggregator:
    def __init__(self):
        # We'll reuse the OpenAI provider for meta-summarization
        self.meta_provider = OpenAIProvider()

    def concatenate(self, responses):
        parts = []
        for i, r in enumerate(responses, start=1):
            parts.append(f"Source {i}:\n{r}")
        return "\n\n".join(parts)

    def meta_summarize(self, original_query, recent_history, provider_results):
        """
        Ask an LLM to synthesize a single answer.
        Keep prompts small for demo purposes.
        """
        # Build a short prompt
        history_text = "\n".join(recent_history) if recent_history else ""
        provider_texts = "\n\n".join([f"{p['provider_name']}:\n{p['response']}" for p in provider_results])
        prompt = (
            "You are MindSharedAI, a meta assistant that receives outputs from several providers. "
            "Your job is to synthesize a single clear, concise, and helpful response to the user's query.\n\n"
            f"User Query:\n{original_query}\n\n"
            f"Recent Conversation Context:\n{history_text}\n\n"
            f"Provider Responses:\n{provider_texts}\n\n"
            "Produce a single final answer. If providers disagree, explain briefly and give the best answer you can."
        )
        return self.meta_provider.query(prompt)

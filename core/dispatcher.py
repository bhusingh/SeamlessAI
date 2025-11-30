"""
Dispatcher: query all configured provider adapters concurrently.
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from providers.openai_provider import OpenAIProvider
from providers.perplexity_provider import PerplexityProvider  # simulated

class Dispatcher:
    def __init__(self, providers=None, max_workers=4):
        # instantiate providers if not provided
        if providers is None:
            providers = [
                OpenAIProvider(),
                PerplexityProvider()
            ]
        self.providers = providers
        self.max_workers = max_workers

    def _call_provider(self, provider, prompt):
        start = time.time()
        try:
            response = provider.query(prompt)
        except Exception as e:
            response = f"[ERROR from {provider.name()}: {str(e)}]"
        latency = time.time() - start
        return {
            "provider_name": provider.name(),
            "response": response,
            "latency": latency
        }

    def query_all(self, prompt):
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as ex:
            futures = {ex.submit(self._call_provider, p, prompt): p for p in self.providers}
            for fut in as_completed(futures):
                results.append(fut.result())
        # keep an order (provider list order)
        # reorder results to match providers list
        name_to_result = {r['provider_name']: r for r in results}
        ordered = [name_to_result[p.name()] for p in self.providers]
        return ordered

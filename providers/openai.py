"""
OpenAI provider adapter (synchronous).
Wraps OpenAI ChatCompletion (Chat Completions / newer API).
"""

import os
import time
import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    # user will be told to set .env; but we avoid hard crash in import to allow some testing
    openai.api_key = None
else:
    openai.api_key = OPENAI_API_KEY

class OpenAIProvider:
    def __init__(self, model="gpt-4o", temperature=0.2, timeout=60):
        # Use a reasonable model default; change to "gpt-5" if your account has access
        self._model = model
        self._temperature = temperature
        self._timeout = timeout

    def name(self):
        return f"OpenAI ({self._model})"

    def query(self, prompt):
        """
        Simple chat completion wrapper. If new API (responses) available change accordingly.
        """
        if openai.api_key is None:
            raise RuntimeError("OPENAI_API_KEY not set. Please add it to .env or environment variables.")
        # Keep messages short for demo
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
        # ChatCompletion endpoint
        resp = openai.ChatCompletion.create(
            model=self._model,
            messages=messages,
            temperature=self._temperature,
            max_tokens=512,
            request_timeout=self._timeout
        )
        # The exact structure may vary slightly by SDK version
        return resp.choices[0].message.content.strip()

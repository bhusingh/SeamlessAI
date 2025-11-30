"""
OpenAI provider adapter (synchronous) - Updated for openai>=1.0.0
"""

import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class OpenAIProvider:
    def __init__(self, model="gpt-4o", temperature=0.2, timeout=60):
        self._model = model
        self._temperature = temperature
        self._timeout = timeout
        
        if not OPENAI_API_KEY:
            self.client = None
        else:
            self.client = OpenAI(api_key=OPENAI_API_KEY, timeout=timeout)

    def name(self):
        return f"OpenAI ({self._model})"

    def query(self, prompt):
        """
        Query OpenAI using the new SDK (v1.0.0+).
        """
        if self.client is None:
            raise RuntimeError("OPENAI_API_KEY not set. Please add it to .env or environment variables.")
        
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
        
        response = self.client.chat.completions.create(
            model=self._model,
            messages=messages,
            temperature=self._temperature,
            max_tokens=512
        )
        
        return response.choices[0].message.content.strip()

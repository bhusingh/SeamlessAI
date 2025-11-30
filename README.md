# SeamlessAI (MVP)

SeamlessAI is a minimal prototype to maintain **seamless, persistent user context across multiple LLM providers** and synthesize a coherent response.

This MVP supports:
- OpenAI (GPT family) as a provider
- A simulated "Perplexity" provider (adapter pattern — replace with a real provider adapter later)
- Per-user JSON memory
- Aggregation: simple concat or meta-summarization (via OpenAI)
- Streamlit UI for quick testing

## Setup

1. Create a Python venv and install:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

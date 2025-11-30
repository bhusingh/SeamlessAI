# MindSharedAI

**Unified AI context layer across multiple LLM providers.**

MindSharedAI maintains seamless, persistent user context across ChatGPT, Perplexity, and other LLM providers—synthesizing coherent responses that feel like talking to a single, informed assistant.

## 🎯 Core Idea

Instead of isolated conversations in each LLM:
- Query ChatGPT → get an answer
- Switch to Perplexity → lose context
- Start over

**With MindSharedAI:**
- One unified context across all providers
- Ask ChatGPT, then Perplexity, and they both know your conversation history
- Responses synthesized into one coherent answer

## ✨ MVP Features

- ✅ **Multi-provider dispatch** — Query OpenAI (GPT-4o) + Perplexity + Claude APIs concurrently
- ✅ **Persistent context** — Per-user memory stored in JSON (SQLite/DB coming soon)
- ✅ **Smart aggregation** — Combine responses via concatenation or meta-summarization
- ✅ **Adapter pattern** — Easy to add more LLM providers
- ✅ **Streamlit UI** — Quick testing interface

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- OpenAI API key (get one at https://platform.openai.com/account/api-keys)

### Install & Run

```bash
# Clone repo
git clone https://github.com/bhusingh/mindshared.git
cd mindshared

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
cp .env.example .env
# Edit .env and add your OpenAI API key
nano .env

# Run the app
streamlit run main.py
```

Open your browser to `http://localhost:8501` 🎉

## 📖 How It Works

### Architecture

```
User Query
    ↓
Context Manager (loads per-user history)
    ↓
Dispatcher (sends to provider APIs concurrently)
    ├─→ OpenAI ChatGPT API
    ├─→ Perplexity API
    └─→ Anthropic Claude API
    ↓
Aggregator (synthesizes responses)
    ├─ Option 1: Concatenate (simple)
    └─ Option 2: Meta-summarize (LLM synthesizes one answer)
    ↓
Response + Context Update
```

### Providers

**OpenAI Provider**
- Model: `gpt-4o` (change to `gpt-5` if available)
- Temperature: 0.2 (factual)

**Perplexity Provider**
- Uses real Perplexity API (when available)
- Fallback to simulated for testing

**Claude Provider**
- Coming in v2.0

### Context Storage

User conversations stored in `user_context.json`:
```json
{
  "user1": [
    "User: What is machine learning?",
    "MindSharedAI: Machine learning is...",
    "User: Tell me about neural networks.",
    "MindSharedAI: Neural networks are..."
  ]
}
```

## 🧪 Testing

1. Enter a **User ID** (e.g., `user1`)
2. Ask a **Query** (e.g., "What is machine learning?")
3. Select **Aggregation mode**:
   - `concatenate`: Simple side-by-side responses
   - `meta-summarize`: LLM synthesizes into one coherent answer
4. Click **Submit** and watch responses stream in

**Test context persistence:**
- Ask a follow-up question (e.g., "Tell me about neural networks based on what we discussed")
- MindSharedAI remembers your first question ✅

## 📂 Project Structure

```
mindshared/
├── main.py                      # Streamlit UI entry point
├── providers/
│   ├── __init__.py
│   ├── openai_provider.py       # OpenAI adapter
│   └── perplexity_provider.py   # Perplexity adapter
├── core/
│   ├── __init__.py
│   ├── context_manager.py       # Per-user memory (JSON storage)
│   ├── dispatcher.py            # Concurrent multi-provider queries
│   └── aggregator.py            # Response synthesis
├── requirements.txt             # Dependencies
├── .env.example                 # Environment variables template
├── README.md                    # This file
└── LICENSE                      # MIT License
```

## 🔧 Configuration

Edit `.env`:

```bash
OPENAI_API_KEY=sk-your-actual-key-here
```

Optional settings in provider files:
- `openai_provider.py`: Change `model="gpt-4o"` to `"gpt-5"` if available
- Add Perplexity API key when integrating real API

## 🛣️ Roadmap

| Version | Status | Timeline | Focus |
|---------|--------|----------|-------|
| **v1.0** | ✅ Complete | Now | Python backend MVP, Streamlit UI, multi-provider dispatch |
| **v1.1** | 🔄 Next | 1-2 weeks | Chrome extension (ChatGPT/Perplexity sidebar integration) |
| **v1.2** | 📋 Planned | 2-3 weeks | Deploy backend to cloud (Railway/Render) |
| **v2.0** | 📋 Planned | Month 1-2 | Real Perplexity API, Claude full integration |
| **v2.1** | 📋 Planned | Month 2 | Vector embeddings, semantic deduplication, smarter context |
| **v3.0** | 📋 Later | Q2 2026 | Multi-user SaaS, auth, hosting (if needed) |

### Why this roadmap?

- **v1.1 Chrome extension** is where the real UX magic happens—users won't leave ChatGPT
- **v1.2 Cloud deployment** makes the extension actually useful (no localhost requirement)
- **v2.x improvements** focus on AI quality (better context, real APIs)
- **v3.0 SaaS** only if we want to commercialize (optional)

## 🚨 Known Limitations

- **Perplexity adapter is simulated** — Uses OpenAI with different prompts until real API is available
- **JSON storage** — Suitable for testing; will migrate to SQLite/PostgreSQL for production
- **No auth** — Single-user mode; multi-user coming in v3.0
- **Streamlit UI** — Good for testing; real UX will be Chrome extension

## 🤝 Contributing

We'd love contributions! Priority areas:

- ✅ **v1.1:** Chrome extension integration
- ✅ **v1.1:** Real Perplexity API adapter
- ✅ **v2.0:** Claude provider adapter
- ✅ **v2.0:** Gemini provider adapter
- ✅ **v2.1:** Vector embeddings for context
- ✅ **General:** Database backend (SQLite/PostgreSQL)
- ✅ **General:** Better error handling & logging

## 📜 License

MIT License — See [LICENSE](LICENSE) for details.

## 👤 Author

Built by [@bhusingh](https://github.com/bhusingh)

## 💬 Questions?

- Open an [issue](https://github.com/bhusingh/mindshared/issues)
- Check [discussions](https://github.com/bhusingh/mindshared/discussions)

---

**Status:** Early MVP in active development. Star ⭐ to follow progress!
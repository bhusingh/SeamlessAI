"""
SeamlessAI - MVP Entry (Streamlit)
"""

import os
from dotenv import load_dotenv
import streamlit as st
from core.context_manager import ContextManager
from core.dispatcher import Dispatcher
from core.aggregator import Aggregator

load_dotenv()  # load OPENAI_API_KEY from .env if present

st.set_page_config(page_title="SeamlessAI - MVP", layout="centered")
st.title("SeamlessAI — Cross-LLM Context MVP")

# UI inputs
user_id = st.text_input("User ID", value="user1")
query = st.text_area("Your query", value="", height=120)
agg_mode = st.selectbox("Aggregation mode", ["concatenate", "meta-summarize"])
submit = st.button("Submit")

# Initialize core components
ctx = ContextManager()          # reads/writes user_context.json
dispatcher = Dispatcher()       # queries provider adapters
aggregator = Aggregator()       # merges/summarizes responses

if submit:
    if not query.strip():
        st.error("Please enter a query.")
    else:
        with st.spinner("Loading context..."):
            history = ctx.load_context(user_id)

        # Build a prompt that includes recent history (simple approach)
        # We'll include last N entries to avoid overly long prompts
        N_HISTORY = 6
        relevant_history = history[-N_HISTORY*2:]  # our history stores alternating user/query and assistant/response
        context_text = "\n".join(relevant_history)

        # Create the dispatched prompt (provider adapters may reformat it)
        prompt_for_providers = f"{context_text}\n\nUser: {query}" if context_text else f"User: {query}"

        st.markdown("**Sending to providers...**")
        with st.spinner("Querying providers (concurrent)..."):
            results = dispatcher.query_all(prompt_for_providers)

        st.markdown("### Provider responses")
        for r in results:
            st.markdown(f"**{r['provider_name']}** (latency: {r['latency']:.2f}s)")
            st.code(r['response'][:400] + ("..." if len(r['response'])>400 else ""))

        st.markdown("---")
        st.markdown("### Aggregated response")
        if agg_mode == "concatenate":
            final = aggregator.concatenate([r['response'] for r in results])
        else:
            # meta-summarize uses OpenAI internally; aggregator will call OpenAI to synthesize
            final = aggregator.meta_summarize(query, relevant_history, results)

        st.text_area("SeamlessAI Response", final, height=300)

        # Update the context: append user query and assistant final answer
        history.append(f"User: {query}")
        history.append(f"SeamlessAI: {final}")
        ctx.save_context(user_id, history)

        st.success("Done — context saved.")

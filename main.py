from llm_dispatcher import query_gpt5, query_local_llm
from context_manager import load_context, save_context
from aggregator import simple_merge
import streamlit as st

st.title("Multi-LLM MVP")

user_id = st.text_input("User ID", "user1")
user_query = st.text_input("Your Query:")

if st.button("Submit"):
    context = load_context(user_id)
    full_prompt = "\n".join(context + [user_query])
    
    # Query LLMs
    gpt5_resp = query_gpt5(full_prompt)
    local_resp = query_local_llm(full_prompt)
    
    # Merge responses
    final_resp = simple_merge([gpt5_resp, local_resp])
    
    # Show output
    st.text_area("Response", final_resp, height=300)
    
    # Update context
    context.append(user_query)
    context.append(final_resp)
    save_context(user_id, context)

import openai
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Set your API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Load local LLM (e.g., MPT-7B)
tokenizer = AutoTokenizer.from_pretrained("mosaicml/mpt-7b-instruct")
model = AutoModelForCausalLM.from_pretrained("mosaicml/mpt-7b-instruct", device_map="auto")

def query_gpt5(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-5",  # replace with correct GPT-5 identifier
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

def query_local_llm(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

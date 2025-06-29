import streamlit as st
import json
import torch
from sentence_transformers import SentenceTransformer, util
import openai
import os
from dotenv import load_dotenv

# 🔐 Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
#Assign key to openai client
openai.api_key = openai_api_key

# === Load semantic model ===
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# === Load intents from JSON ===
@st.cache_data
def load_intents():
    with open("intents.json") as f:
        return json.load(f)

data = load_intents()

# Prepare patterns & responses
patterns = []
responses = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        responses.append(intent["responses"][0])
        tags.append(intent["tag"])

# Precompute pattern embeddings
pattern_embeddings = model.encode(patterns, convert_to_tensor=True)

# === Semantic Similarity Matcher ===
def get_semantic_response(user_input, threshold=0.55):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(user_embedding, pattern_embeddings)
    best_idx = torch.argmax(cosine_scores)
    best_score = cosine_scores[0][best_idx].item()

    if best_score >= threshold:
        return responses[best_idx], best_score
    else:
        return None, best_score

# === GPT-4 Fallback ===
def gpt_fallback(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful educational chatbot for Yabatech, Nigeria. Answer clearly and accurately."},
                {"role": "user", "content": user_input}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error contacting GPT: {str(e)}"

# === Streamlit UI ===
st.set_page_config(page_title="YabatechEduBot", page_icon="🎓")
st.title("🤖 YabatechEduBot")
st.caption("Ask me anything about admissions, courses, fees, or more.")

user_input = st.text_input("Type your question:")

if user_input:
    # Try semantic match first
    response, score = get_semantic_response(user_input)

    # If no good match, fall back to GPT
    if response:
        st.success(f"💬 {response}")
        st.caption(f"Matched using semantic similarity (score: {round(score, 2)})")
    else:
        st.info("No good match found. Asking GPT...")
        gpt_response = gpt_fallback(user_input)
        st.success(f"🧠 {gpt_response}")

import streamlit as st
import json
from sentence_transformers import SentenceTransformer, util
import torch

# Load the model once and cache it
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# Load intents from the JSON file
@st.cache_data
def load_intents():
    with open("intents.json") as f:
        return json.load(f)

data = load_intents()

# Prepare patterns and responses lists
patterns = []
responses = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        responses.append(intent["responses"][0])

# Encode patterns once
pattern_embeddings = model.encode(patterns, convert_to_tensor=True)

def get_response(user_input, threshold=0.55):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(user_embedding, pattern_embeddings)
    best_idx = torch.argmax(cosine_scores)
    best_score = cosine_scores[0][best_idx].item()

    if best_score >= threshold:
        return responses[best_idx]
    else:
        return "Sorry, I didn't understand that. Could you please rephrase?"

# Streamlit App Interface
st.set_page_config(page_title="YabatechEduBot", page_icon="🤖")
st.title("🤖 YabatechEduBot")
st.write("Ask me anything about applying, courses, greetings, and more!")

user_input = st.text_input("Type your question:")

if user_input:
    answer = get_response(user_input)
    st.success(answer)

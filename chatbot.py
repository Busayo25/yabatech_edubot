import json
import random
import nltk
import pickle
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

with open("intents.json") as f:
    intents = json.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def clean_text(text):
    tokens = text.lower().split()
    return " ".join([stemmer.stem(word) for word in tokens])

def get_response(user_input):
    cleaned = clean_text(user_input)
    X = vectorizer.transform([cleaned])
    tag = model.predict(X)[0]

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "I'm not sure how to respond to that."

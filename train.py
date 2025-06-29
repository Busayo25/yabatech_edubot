import json
import random
import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import pickle

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
nltk.download("punkt")

# Load intents
with open("intents.json") as file:
    data = json.load(file)

corpus = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern.lower())
        stemmed = [stemmer.stem(w) for w in tokens]
        corpus.append(" ".join(stemmed))
        labels.append(intent["tag"])

# Vectorization and model training
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
model = MultinomialNB()
model.fit(X, labels)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
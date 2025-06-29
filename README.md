# 📚 YabatechEdubot 🤖

**YabatechEdubot** is an interactive educational chatbot designed to assist students and prospective applicants of **Yaba College of Technology**. It answers questions about admissions, departments, courses, fees, and more — all powered by Natural Language Processing (NLP) and machine learning.

![Streamlit App Screenshot](https://imgur.com/a/placeholder) <!-- You can add your own screenshot URL later -->

---

## 🚀 Features

- Built using **Streamlit** for a simple, responsive UI
- Trained using **NLTK** and **Scikit-learn**
- Learns from a structured `intents.json` file
- Predicts user intent and gives meaningful answers
- Fast, light, and mobile-friendly

---

## 📁 Folder Structure

yabatech_edubot/ 
├── app.py    # Streamlit web app ├── chatbot.py # Logic for response generation 
├── train.py # Trains and saves the model 
├── intents.json # Training data (intents + responses) 
├── model.pkl # Trained Naive Bayes model 
├── vectorizer.pkl # Fitted CountVectorizer 
└── requirements.txt # Python dependencies

---

## 🛠 How to Run Locally

### 🧰 Prerequisites:
- Python 3.x installed
- Streamlit, nltk, scikit-learn

### 🔄 Setup:

```bash
git clone https://github.com/YOUR_USERNAME/yabatech_edubot.git
cd yabatech_edubot
pip install -r requirements.txt

▶️ Run the chatbot:

streamlit run app.py


---

🌐 Live Demo

Deployed on Streamlit Cloud:
👉 https://yabatech-edubot.streamlit.app (Replace with your real URL once deployed)


---

🙌 Contributions

Have more Yabatech questions or new intents to add?
Feel free to:

Fork the repo

Add more patterns and responses to intents.json

Retrain using train.py

Submit a pull request!



---

👨‍💻 Creator

Busayo Elijah
Passionate about education, AI, and student empowerment.


---

🪪 License

This project is open-source and available under the MIT License.

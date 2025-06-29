# 🤖 YabatechEduBot

A hybrid educational chatbot built with Streamlit that answers questions about Yabatech admissions, courses, fees, and more.  
It combines semantic similarity matching with OpenAI's GPT-4 to intelligently handle both known and unseen questions.

---

## Features

- **Semantic Search:** Matches user questions against a large dataset of predefined intents for quick, accurate answers.  
- **GPT-4 Fallback:** Uses OpenAI’s GPT-4 API to generate natural, relevant responses for unseen or complex questions.  
- **Streamlit UI:** Simple and interactive web interface accessible on desktop and mobile.  
- **Secure API Key Handling:** Uses environment variables and Streamlit Secrets to securely manage OpenAI API keys.  

---

## Demo

[Add your deployed Streamlit app link here]

---

## Installation & Setup

### Prerequisites

- Python 3.7 or higher  
- An OpenAI API key ([Get yours here](https://platform.openai.com/signup))  
- Git (optional, for cloning this repo)

### Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Install dependencies

pip install -r requirements.txt

Setup environment variables

Create a .env file in the project root (do not commit this file):

OPENAI_API_KEY=your_openai_api_key_here

Alternatively, if deploying on Streamlit Cloud, add this key in the app’s Secrets settings.


---

Running the App Locally

streamlit run app.py

Open your browser to http://localhost:8501 and start chatting!


---

Deployment

You can deploy this app on Streamlit Cloud:

1. Push your code to a GitHub repo.


2. Create a new Streamlit app linked to your repo.


3. Add your OpenAI API key in the Secrets section.


4. Deploy and share!




---

Project Structure

├── app.py            # Main Streamlit app with semantic + GPT-4 logic
├── intents.json      # Dataset of predefined questions and responses
├── requirements.txt  # Python dependencies
├── .gitignore        # Files to ignore in Git
├── README.md         # This file


---

How It Works

1. User inputs a question in the UI.


2. The app tries to find a matching question using sentence-transformers semantic similarity.


3. If a confident match is found, it returns the matched answer.


4. If not, it sends the question to OpenAI GPT-4 and returns the AI-generated answer.




---

Contributing

Contributions are welcome! Feel free to:

Add more questions and responses to intents.json

Improve UI/UX in app.py

Enhance the fallback or caching logic


Please open issues or pull requests for suggestions and fixes.


---

License

MIT License


---

Contact

Your Name — oguntugabusayo19@gmail.com
Project Link: https://github.com/Busayo25/

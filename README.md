# 🤖 Flask ChatBot by Vineet

A lightweight, modular AI-powered chatbot built with **Python**, **Flask**, and **OpenAI**, capable of answering real-world queries, evaluating math expressions, responding to user greetings, remembering names, and fetching live **weather** and **Wikipedia** information.

https://github.com/user-attachments/assets/d97b584b-f402-4ef2-97fc-45f00141d7c0

---

## ✨ Features

- ✅ Conversational AI with OpenAI GPT
- 🌦 Live Weather Info via OpenWeather API
- 🧠 Wikipedia summaries via `wikipedia` module
- 🧮 Math expression evaluation (e.g., `2+2*5`)
- 🕐 Current Date & Time
- 👋 Name recognition (`My name is Vineet`)
- 💬 Intelligent greeting replies
- 🌐 Flask web interface (responsive)

---

## 📁 Project Structure

flask_chatbot/
│
├── app.py # Flask app
├── bot_logic.py # Core logic and integrations
├── templates/
│ └── index.html # Frontend (Jinja2)
├── static/
│ ├── logo.jpg # Bot logo (optional)
│ └── bg.jpg # Background image (optional)
├── secrets.py # 🔒 Store your API keys (excluded from Git)
├── config.py # Placeholder for keys (excluded from Git)
├── .gitignore
└── requirements.txt




---

## ⚙️ Setup Instructions

1. **Clone the Repo**
   git clone https://github.com/Vineet0001/Flask-Chatbot.git
   cd Flask-Chatbot

2. **Create and Activate Virtual Environment (optional)**
   python -m venv venv
   venv\Scripts\activate  # On Windows

4. **Install Dependencies**
   pip install -r requirements.txt

5. **Add your API keys**
   secrets.py
   OPENWEATHER_API_KEY = "your_openweather_api_key"
   OPENAI_API_KEY = "your_openai_api_key"

6. **🚀 Run the Application**
   python app.py  --Then open your browser at:
  📍 http://127.0.0.1:5000

## 📌To-Do / Future Ideas

   Add persistent chat history

   Support voice-to-text

   Deploy on Render / Railway / Vercel

## 🧠Tech Stack
   Python 3.10+

   Flask + Jinja2

   OpenAI GPT API

   OpenWeather API

   Wikipedia (Python lib)



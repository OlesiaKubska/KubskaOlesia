# 👩‍👧‍👦 MomBoss Family Planner – Agentic AI Hackathon 2025

Welcome to my hackathon project! 
This AI agent helps **busy moms with multiple children** organize meaningful family time by using natural language input to generate activity plans and automatically schedule events in Google Calendar.

---

## 🧠 What It Does

👤 User types any request (e.g. _"Plan something fun for my kids this weekend"_)

📋 Agent breaks it into steps using a task planner

🔑 It calls Google Gemini API to enhance output

🗂 Saves the plan to file in `plans/`

📅 Automatically creates a Google Calendar event via OAuth

---

## 🚀 How to Run

1. **Clone the repository**  
```bash
git clone https://github.com/OlesiaKubska/KubskaOlesia.git
cd KubskaOlesia
```

2. **Install requirements**

```bash
pip install -r requirements.txt
```

3. **Create .env file with Gemini API key**

```ini
GEMINI_API_KEY=your_key_here
```

4. **Make sure you have credentials.json (not committed) for Google Calendar API**

- Enable Google Calendar API

- Download credentials.json to src/

5. **Run the app**

```bash
python src/main.py
```

## 📁 Project Structure

```bash

├── src/
│   ├── main.py                 # Main agent loop
│   ├── planner.py              # Task planner
│   ├── executor.py             # Gemini API call
│   ├── memory.py               # Memory logging
│   └── calendar_integration.py # Google Calendar integration
├── plans/                      # Saved plans
├── .env                        # Secret API key (not tracked)
├── .gitignore
├── README.md
├── ARCHITECTURE.md
├── EXPLANATION.md
├── DEMO.md
```

## 🔧 Technologies

- 🐍 Python 3.13

- 🌐 Google Gemini API

- 📅 Google Calendar API (OAuth2)

- 💾 dotenv, google-auth, google-api-python-client

## 📌 Features
- ✅ Conversational AI agent

- 🧠 Task planning logic

- 🧩 Gemini integration

- 🗓 Google Calendar auto events

- 📝 Plan history saved to .txt

## ⚠️ Notes
- credentials.json and token.pickle are excluded via .gitignore

- Make sure Google OAuth is set up locally for Calendar access

- Token is stored as token.pickle after the first run

## 🎥 Demo
See [DEMO.md](DEMO.md) for a link to the walkthrough video with timestamps.

## 🏁 Good luck to all hackers!
Made with 💡 and ☕ by Olesia Kubska

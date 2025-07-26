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

3. **Set up environment variables**
Create a `.env` file in the root directory and add your Gemini API key:

```ini
GEMINI_API_KEY=your_gemini_api_key_here
```

4. **Set up Google Calendar**

- Enable [Google Calendar API](https://console.cloud.google.com/apis/library/calendar-json.googleapis.com)

- Download `credentials.json` file
  
- Place it in the `src/` folder

5. **Run the App with UI (Streamlit)**

```bash
streamlit run src/app.py
```

The frontend will open in your browser at:
`http://localhost:8501`

---

## 📁 Project Structure

```bash

├── src/
│   ├── app.py                  # Streamlit UI with Gemini agent
│   ├── main.py                 # Main agent loop
│   ├── planner.py              # Task planner
│   ├── executor.py             # Gemini API interaction
│   ├── memory.py               # Saves responses and logs inputs
│   └── calendar_integration.py # Google Calendar integration
├── plans/                      # Saved text plans from the user
├── memory_log.txt             # Input history log
├── .env                        # API key (not committed)
├── .gitignore
├── requirements.txt
├── README.md
├── ARCHITECTURE.md            # Architecture diagram
├── EXPLANATION.md             # Explanation of how it works
├── DEMO.md                    # Video link with timestamps
```

---

## 🔧 Technologies

- 🐍 Python 3.13

- 🌐 Google Gemini API

- 📅 Google Calendar API (OAuth2)

- 💾 `dotenv`, `google-auth`, `google-api-python-client`
  
- 🖥️ Streamlit – UI для взаємодії з агентом

---

## 📌 Features
- ✅ Conversational AI agent

- 🧠 Task planning logic (via `planner.py`)

- 🧩 Gemini API integration for rich, personalized plans

- 🗓 Google Calendar auto events (via OAuth2)

- 📝 Plans saved as readable `.txt` files in `plans/`
  
- 💬 **Streamlit-based UI** for easy interaction
  
- 🔁 **“View Last” command** to retrieve your most recent plan
  
- 🕓 **“History” command** to show last 5 input queries
  
- ✍️ Modular design with memory logging (`memory.py`)

---

## ⚠️ Notes
- `credentials.json` and `token.pickle` are excluded via `.gitignore`

- Make sure Google OAuth is set up locally for Calendar access

- Token is stored as `token.pickle` after the first run
  
- **The app UI runs via** `app.py` **using Streamlit**
  
- Do not expose your `.env` file containing the Gemini API key

---

## 🎥 Demo
See [DEMO.md](DEMO.md) for a link to the walkthrough video with timestamps.

---

## 🏁 Good luck to all hackers!
Made with 💡 and ☕ by Olesia Kubska

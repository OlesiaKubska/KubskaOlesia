# 🧱 ARCHITECTURE

This document outlines the architecture of the **"MomBoss Family Planner"**, an AI assistant designed to help busy moms plan fun, balanced days with their children — including automatic calendar integration and simple memory.

---

## ⚙️ Core Workflow

```
┌────────────┐
│  app.py    │ ← Streamlit front-end UI
└────┬───────┘
     │
     ▼
┌──────────────┐
│ planner.py   │ ← Breaks user goal into tasks via prompt
└────┬─────────┘
     ▼
┌──────────────┐
│ executor.py  │ ← Calls Gemini API
└────┬─────────┘
     ▼
┌──────────────┐
│ memory.py    │ ← Saves plan to /plans folder
└────┬─────────┘
     ▼
┌────────────────────────┐
│ calendar_integration.py│ ← Creates Google Calendar event
└────────────────────────┘
```
---

## 🧠 Extra Features

- 🗂 `view last` **command** — Shows last saved plan from `/plans/`

- 📚 `history` **command** — Displays last 5 logged user requests

---

## 🔌 Integrations

- 🧠 **Gemini API (google.generativeai)** – Used for creative plan generation
- 📅 **Google Calendar API (OAuth2)** – Adds events to calendar calendar.
- 🖥 **Streamlit** – Frontend interface

---

## 🧩 File Structure

```
src/
├── app.py                  # Streamlit UI
├── main.py                 # CLI fallback (optional)
├── planner.py              # Task planning
├── executor.py             # Gemini API interaction
├── memory.py               # Logging memory & user input
├── calendar_integration.py # Google Calendar logic
plans/                      # Saved plan .txt files
.env                        # API key (ignored)
memory_log.txt              # Optional user prompt log
```
---

## 📝 Logging & Observability

- ✅ Plans saved to `.txt` in `plans/`

- ✅ User inputs saved to `memory_log.txt`

- ✅ Streamlit console prints Gemini output and event link
  
- ❌ No advanced telemetry, tracing or exception analytics

---

## 🛠 Technologies Used

- Python 3.13
- Streamlit
- Google Gemini API
- Google Calendar API
- `dotenv`, `google-auth`, `google-api-python-client`

---

## 🔐 Secrets & Security

- `.env` contains Gemini API key (not tracked)

- `credentials.json` and `token.pickle` are ignored via `.gitignore`

- Never commit secrets to the repo

---

✅ This modular and UI-enhanced architecture allows for simple expansion — including future Telegram bot integration, memory recall, or family profile customization.




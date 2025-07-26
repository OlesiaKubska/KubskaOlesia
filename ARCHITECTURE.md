# 🧱 ARCHITECTURE

This document outlines the architecture of the **"MomBoss Family Planner"**, an AI assistant designed to help busy moms plan fun, balanced days with their children — including automatic calendar integration.

---

## ⚙️ Core Workflow

```
┌────────────┐
│  main.py   │ ← Central control loop
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

## 🔌 Integrations

- 🧠 **Gemini API** – Handles the logic of natural language planning.

- 📅 **Google Calendar API (OAuth2)** – Adds events directly to user calendar.

---

## 🧩 File Structure

```
src/
├── main.py                 # Main conversation loop
├── planner.py              # Task planning
├── executor.py             # Gemini API interaction
├── memory.py               # Logging memory (plans)
├── calendar_integration.py # Google Calendar logic
plans/                      # Saved plan .txt files
.env                        # API key (ignored)
```
---

## 📝 Logging & Observability

- Logs each plan to a timestamped `.txt` file in `plans/`

- Google Calendar event creation success printed to console with link

- No analytics or telemetry beyond local file logging

---

## 🛠 Technologies Used

- Python 3.13

- dotenv

- google-api-python-client

- google-auth

- google-auth-oauthlib

- Gemini Pro (via `google.generativeai`)

---

## 🔐 Secrets & Security

- `.env` file stores the Gemini API key

- `credentials.json` and `token.pickle` are ignored and not tracked

- All secrets excluded via `.gitignore`

---

This modular design makes it easy to test individual parts, and extend the planner to include memory retrieval or front-end integration in the future.




# Technical Explanation

## 🧠 Smart Agent Design Overview

This document explains how the **"MomBoss Family Planner"** agent works — its reasoning, logic, and tool use.

---

### 1. 👣 Agent Workflow

The agent follows this process:

1. **User Input via Streamlit UI:**
   - User enters a natural language prompt (e.g., "Plan something fun this weekend") through a web-based interface.

2. **Task Planning (`planner.py`):**
   - Breaks the request into subtasks using prompt engineering for Gemini.

3. **Task Execution (`executor.py`):**
   - Uses Gemini Pro to generate a detailed, human-like family schedule.

4. **Save Plan (`memory.py`):**
   - Stores the plan in a timestamped `.txt` file in the `plans/` folder.

5. **Log Input Context (`memory.py`):**
   - Adds the input to a `memory_log.txt` file to support simple memory/history.

6. **Create Google Calendar Event (`calendar_integration.py`):**
   - Generates a simplified version of the plan and pushes it to the user’s Google Calendar.

7. **Output Results in UI:**
   - Full schedule is shown in the app, along with a link to the created calendar event.

8. **Extra Command ("view last"):**
   - Allows the user to view their most recent saved plan on demand.

---

### 2. 🔧 Key Modules

- **`app.py`**  
  - Streamlit-based user interface and input control.

- **`planner.py`**  
  - Breaks down requests into task prompts for Gemini.

- **`executor.py`**  
  - Handles all Gemini API interactions.

- **`memory.py`**  
  - Logs input queries and stores responses to files.

- **`calendar_integration.py`**  
  - Uses Google Calendar API to create events with OAuth2 flow.

---

### 3. 🔌 Tool Integration

- **Gemini API (`google.generativeai`)**
  - Used for generating the plan based on structured prompts.

- **Google Calendar API**
  - Integrated with `google-api-python-client` using `credentials.json` for OAuth2 authentication.

---

### 4. 🕵️ Observability & Testing

- ✅ **Console Logging:**
  - Logs Gemini output and Google Calendar event links.

- ✅ **File Logging:**
  - Full plans saved in `/plans/plan_TIMESTAMP.txt`.

- ✅ **User Input History:**
  - Last 5 inputs stored in `memory_log.txt`.

- ✅ **"view last" Command:**
  - Loads most recent plan in Streamlit UI.

- ❌ **No telemetry, unit tests, or exception tracking tools integrated.**

---

### 5. ⚠️ Known Limitations

- ⏳ Manual OAuth consent required on first Google Calendar access.

- 🧠 No deep memory retrieval or personalization yet (but `memory_log.txt` lays groundwork).

- ❓ May return generic responses for vague prompts.

- 📡 Dependent on internet for Gemini and Calendar APIs.

---

### 🧭 Future Improvements

- Add a full chatbot-style memory loop

- Telegram bot integration for mobile use

- Smart reminders or nudges via calendar

- Child-age-specific plan generation

---

The agent is modular and extensible — future improvements may include GUI, memory recall, or real-time family collaboration features.


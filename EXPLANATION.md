# Technical Explanation

## 🧠 Smart Agent Design Overview

This document explains how the "MomBoss Family Planner" agent works — its reasoning, logic, and tool use.

---

### 1. 👣 Agent Workflow

The agent follows this flow:

  1. **Receive Input:**

User types a message in natural language, e.g., "Plan something fun for my kids this weekend"

  2. **Plan Tasks (planner.py):**

Breaks the user's intent into specific subtasks (e.g., “Find activity,” “Schedule event,” etc.) using a prompt to Gemini.

  3. **Execute Tasks (executor.py):**

Uses Google Gemini Pro to generate a detailed, creative plan from the subtasks.

  4. **Save Plan (memory.py):**

Stores the generated response to a `.txt` file in the `plans/` directory with a timestamp.

  5. **Create Calendar Event (calendar_integration.py):**

Sends a simplified summary to Google Calendar API and returns a calendar event link.

  6. **Output:**

Shows the Gemini response + Google Calendar event link in the console.

---

### 2. 🔧 Key Modules

- **`planner.py`**

  - Prepares structured planning prompt based on user input.

- **`executor.py`**

  - Calls Gemini API to get the main response.

- **`memory.py`**

  - Saves full plan with timestamp for local tracking.

- **`calendar_integration.py`**

  - Creates an event using OAuth and Google Calendar API.

---

### 3. 🔌 Tool Integration

- Gemini API (`google.generativeai`)

  - Used in `executor.py` to generate creative content.

- Google Calendar API

  - Called via `calendar_integration.py` using `google-api-python-client` and `credentials.json`

---

### 4. 🕵️ Observability & Testing

- ✅ Console logging:

  - Prints Gemini response and calendar event creation URL.

- ✅ Local logging:

  - Plans saved in `/plans/` as `.txt` for each user input.

- ❌ No automated test scripts (`TEST.sh`) or external observability tools added yet.

--- 

### 5. ⚠️ Known Limitations

- ⏳ First-time calendar use requires manual OAuth approval

- 🧠 No memory retrieval yet (only save, no read)

- ❓ Ambiguous requests are passed directly to Gemini

- 🐢 May slow down with poor internet during Gemini or Calendar API calls

---

The agent is modular and extensible — future improvements may include GUI, memory recall, or real-time family collaboration features.


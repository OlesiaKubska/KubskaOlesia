# memory.py
import os
from datetime import datetime

def save_memory(user_input, agent_response):
    os.makedirs("plans", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"plans/plan_{timestamp}.txt"

    content = f"🧑 User: {user_input}\n\n🤖 Agent:\n{agent_response}"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"✅ Plan saved to: {filename}")

def log_user_input(user_input):
    with open("memory_log.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"[{timestamp}] {user_input}\n")
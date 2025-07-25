# src/main.py
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
import os
from planner import plan_tasks
from executor import execute_tasks
from memory import save_memory

load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ API key not found. Please check your .env file.")

def main():
    print("👋 Hello! I'm your Agent. Ask me anything.")
    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        tasks = plan_tasks(user_input)
        result = execute_tasks(tasks, API_KEY)
        save_memory(user_input, result)
        print("🤖 Agent:", result)

if __name__ == "__main__":
    main()
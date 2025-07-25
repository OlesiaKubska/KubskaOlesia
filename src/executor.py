import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def execute_tasks(tasks, api_key):
    results = []
    for task in tasks:
        try:
            if task["type"] == "text-generation":
                print("Input to Gemini:", task["input"])
                response = model.generate_content(task["input"])
                print("Gemini Response:", response.text)
                results.append(response.text)
            else:
                results.append("[Unsupported task type]")
        except Exception as e:
            print(f"❌ Request failed: {e}")
            results.append("[Error: failed to get response]")
    return "\n".join(results)
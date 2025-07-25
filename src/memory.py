# memory.py
def save_memory(question, answer):
    with open("memory_log.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {question}\nAgent: {answer}\n\n")
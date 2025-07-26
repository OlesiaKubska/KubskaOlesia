def plan_tasks(user_input):
    tasks = []

    if "schedule" in user_input.lower() or "plan" in user_input.lower():
        tasks.append({
            "type": "text-generation",
            "input": f"Please help plan a day for a busy mom with 4 kids and a business. Request: {user_input}"
        })
        tasks.append({
            "type": "text-generation",
            "input": "Suggest time blocks for family, work, and self-care for a mom managing many tasks."
        })

    elif "gift" in user_input.lower() or "birthday" in user_input.lower():
        tasks.append({
            "type": "text-generation",
            "input": f"Suggest a gift idea for a child. Request: {user_input}"
        })

    elif "help" in user_input.lower() or "idea" in user_input.lower():
        tasks.append({
            "type": "text-generation",
            "input": f"Suggest ideas and next steps for: {user_input}"
        })

    else:
        tasks.append({
            "type": "text-generation",
            "input": user_input  # default fallback
        })

    return tasks
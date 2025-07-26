import streamlit as st
import os
from dotenv import load_dotenv
from planner import plan_tasks
from executor import execute_tasks
from memory import save_memory, log_user_input
from calendar_integration import create_calendar_event

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ API key not found. Please check your .env file.")
    st.stop()

# UI setup
st.set_page_config(page_title="MomBoss Family Planner", page_icon="👩‍👧‍👦")
st.title("👩‍👧‍👦 MomBoss Family Planner")
st.write("Let AI help you plan meaningful time with your children.")

# Time selection
time_block = st.selectbox("🕒 Select time range:", ["Full day", "Morning", "Afternoon"])

# Input
user_input = st.text_input("📄 What would you like to plan?", placeholder="Plan something fun this weekend or type 'view last'...").strip()

# Handle special commands
if user_input.lower() == "view last":
    try:
        plans_dir = "plans/"
        files = sorted([f for f in os.listdir(plans_dir) if f.startswith("plan_")], reverse=True)
        if files:
            last_file = files[0]
            with open(os.path.join(plans_dir, last_file), "r", encoding="utf-8") as f:
                content = f.read()
            st.success("✅ Last Plan:")
            st.text_area("🗂️ View Last Plan", content, height=400)
        else:
            st.warning("No saved plans found.")
    except Exception as e:
        st.error(f"⚠️ Could not load last plan: {e}")

elif user_input.lower() == "history":
    try:
        with open("memory_log.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()[-5:]  # Last 5 entries
            st.success("📚 Last Inputs:")
            st.text("".join(lines))
    except FileNotFoundError:
        st.warning("No history found yet.")

elif user_input == "":
    st.info("Please enter a request to generate a plan or type 'view last' or 'history'.")

# Generate plan
elif st.button("Generate Plan"):
    with st.spinner("🧠 Thinking..."):
        final_input = f"""
        You're a professional family assistant who helps busy moms manage their day. 
        Generate a detailed, realistic, and fun schedule based on this user request: "{user_input}".
        Make the schedule specific for the {time_block.lower()}.

        Use the following format:
        ## [Title of the Plan]

        **Goal:** [Short 1-sentence purpose of this block]

        **Time** | **Activity** | **Details/Tips**
        -------- | ------------ | ----------------
        6:00 AM  | Example Task | Short description...

        Make sure to:
        - Balance structure with flexibility.
        - Include both responsibilities and bonding time.
        - Use times in 15–30 minute blocks.
        """

        tasks = plan_tasks(final_input)
        response = execute_tasks(tasks, api_key=API_KEY)
        save_memory(user_input=final_input, agent_response=response)
        log_user_input(user_input)
        link = create_calendar_event(response)

        st.success("✅ AI Plan")
        st.markdown(response)

        if link:
            st.markdown(f"[📅 View Calendar Event]({link})")

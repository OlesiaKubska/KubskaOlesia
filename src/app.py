import streamlit as st
from planner import plan_tasks
from executor import execute_tasks
from memory import save_memory
from calendar_integration import create_calendar_event
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ API key not found. Please check your .env file.")
    st.stop()

st.set_page_config(page_title="MomBoss Family Planner", page_icon="👩‍👧‍👦")

st.title("👩‍👧‍👦 MomBoss Family Planner")
st.write("Let AI help you plan meaningful time with your children.")

user_input = st.text_input("📝 What would you like to plan?", placeholder="Plan something fun this weekend...")

if st.button("Generate Plan") and user_input:
    with st.spinner("🧠 Thinking..."):
        tasks = plan_tasks(user_input)
        result = execute_tasks(tasks, API_KEY)
        save_memory(user_input, result)
        event_link = create_calendar_event(user_input)

    st.subheader("✅ AI Plan")
    st.write(result)

    if event_link:
        st.success(f"📅 Calendar Event Created! [View it here]({event_link})")
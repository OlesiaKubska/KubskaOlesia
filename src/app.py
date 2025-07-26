import streamlit as st
import os
from dotenv import load_dotenv
from planner import plan_tasks
from executor import execute_tasks
from memory import save_memory
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
user_input = st.text_input("📄 What would you like to plan?", placeholder="Plan something fun this weekend or type 'view last'...")

# Check for 'view last'
if user_input.lower() == "view last":
    try:
        plans_dir = "plans/"
        last_file = sorted(os.listdir(plans_dir))[-1]
        with open(os.path.join(plans_dir, last_file), "r", encoding="utf-8") as f:
            content = f.read()
        st.success("✅ Last Plan:")
        st.markdown(content)
    except Exception as e:
        st.error(f"⚠️ Could not load last plan: {e}")

# Generate plan
if st.button("Generate Plan") and user_input.lower() != "view last":
    with st.spinner("🎀 Thinking..."):
        # Include time block in prompt
        final_input = f"{user_input}. Please make a {time_block.lower()} plan."
        tasks = plan_tasks(final_input)
        response = execute_tasks(tasks, api_key=API_KEY)
        save_memory(user_input=final_input, agent_response=response)
        link = create_calendar_event(response)

        st.success("✅ AI Plan")
        st.markdown(response)

        if link:
            st.markdown(f"[📅 View Calendar Event]({link})")
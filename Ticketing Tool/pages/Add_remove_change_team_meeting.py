import streamlit as st
import datetime

st.title("📅 Add / Remove / Change Team Meeting")

with st.form("team_meeting_form"):
    meeting_action = st.selectbox("What are we updating for the meeting? *", [
        "Meeting End time", "Cancel Meeting", "Add Meeting"
    ])
    meeting_duration = st.number_input("How long is the meeting? (in minutes) *", min_value=1, max_value=999)
    inquiry_week = st.date_input("Which week are you inquiring for? (enter the Monday) *")
    notes = st.text_area("Additional Notes (e.g. CP3 approval, context)")

    submitted = st.form_submit_button("Submit Meeting Request")

if submitted:
    st.success("✅ Meeting request submitted.")
    # Add logic to save or pass data back to main ticket
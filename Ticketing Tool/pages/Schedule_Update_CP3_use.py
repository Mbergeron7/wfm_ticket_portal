import streamlit as st

st.title("📆 Schedule Update (CP3 Use)")

with st.form("schedule_update_form"):
    # New schedule times
    new_start_time = st.text_input("New Start Time * (HH:MM AM/PM)")
    new_end_time = st.text_input("New End Time * (HH:MM AM/PM)")
    
    # CP3 approval
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "jpg", "png"])
    
    # Notes
    notes = st.text_area("Additional Notes (e.g. reason for update, context)")

    submitted = st.form_submit_button("Submit Schedule Update")

if submitted:
    st.success("✅ Schedule update submitted.")
    # Add logic to save or pass data back to main ticket
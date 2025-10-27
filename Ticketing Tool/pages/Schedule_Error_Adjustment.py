import streamlit as st

st.title("🕒 Schedule Error Adjustment")

with st.form("schedule_error_form"):
    # Old times
    st.markdown("### ⏪ Old Times")
    old_start_1 = st.text_input("Old Start Time 1 (HH:MM AM/PM)")
    old_start_2 = st.text_input("Old Start Time 2 (HH:MM AM/PM)")
    old_end_1 = st.text_input("Old End Time 1 (HH:MM AM/PM)")
    old_end_2 = st.text_input("Old End Time 2 (HH:MM AM/PM)")

    # New times
    st.markdown("### ⏩ New Times")
    new_start_1 = st.text_input("New Start Time 1 (HH:MM AM/PM)")
    new_start_2 = st.text_input("New Start Time 2 (HH:MM AM/PM)")
    new_start_3 = st.text_input("New Start Time 3 (HH:MM AM/PM)")
    new_end_1 = st.text_input("New End Time 1 (HH:MM AM/PM)")
    new_end_2 = st.text_input("New End Time 2 (HH:MM AM/PM)")
    new_end_3 = st.text_input("New End Time 3 (HH:MM AM/PM)")

    # Segment update
    segment_action = st.selectbox("Are we adding or removing a segment? *", ["Adding", "Removing"])
    segment_type = st.selectbox("Which segment is being updated? *", [
        "After Shift", "Client Account Work", "Coaching", "Code of Conduct", "Knowledge Assessment",
        "Leader on Duty", "Meeting", "Personal", "Spirit Committee", "System Issue", "System Outage"
    ])

    # CP3 approval
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "jpg", "png"])
    notes = st.text_area("Additional Notes")

    submitted = st.form_submit_button("Submit Schedule Adjustment")

if submitted:
    st.success("✅ Schedule adjustment submitted.")
    # Add logic to save or pass data back to main ticket
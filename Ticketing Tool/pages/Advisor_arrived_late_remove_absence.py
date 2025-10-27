import streamlit as st

st.title("⏰ Advisor Arrived Late — Remove Absence")

with st.form("late_arrival_form"):
    # Old times
    st.markdown("### ⏪ Original Times")
    old_start_time = st.text_input("Old Start Time * (HH:MM AM/PM)")
    old_end_time = st.text_input("Old End Time * (HH:MM AM/PM)")

    # New times
    st.markdown("### ⏩ Corrected Times")
    new_start_time = st.text_input("New Start Time * (HH:MM AM/PM)")
    new_end_time = st.text_input("New End Time * (HH:MM AM/PM)")

    # Segment update
    segment_action = st.selectbox("Are we adding or removing a segment? *", ["Adding", "Removing"])
    segment_type = st.selectbox("Which segment is being updated? *", [
        "After Shift", "Client Account Work", "Coaching", "Code of Conduct", "Knowledge Assessment",
        "Leader on Duty", "Meeting", "Personal", "Spirit Committee", "System Issue", "System Outage"
    ])

    # CP3 approval
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "jpg", "png"])
    notes = st.text_area("Additional Notes")

    submitted = st.form_submit_button("Submit Absence Correction")

if submitted:
    st.success("✅ Absence correction submitted.")
    # Add logic to save or pass data back to main ticket
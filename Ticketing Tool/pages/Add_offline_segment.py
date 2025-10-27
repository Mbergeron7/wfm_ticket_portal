import streamlit as st

st.title("📴 Add Offline Segment")

with st.form("offline_segment_form"):
    segment_name = st.selectbox("Name of Segment to Update *", [
        "After Shift", "Client Account Work", "Coaching", "Code of Conduct", "Knowledge Assessment",
        "Meeting", "Personal", "Store Visit", "System Issue", "System Outage", "Training"
    ])
    segment_action = st.selectbox("Are we adding, removing or updating the segment? *", [
        "Adding", "Removing", "Updating"
    ])
    new_start_time = st.text_input("New Start Time * (HH:MM AM/PM)")
    new_end_time = st.text_input("New End Time * (HH:MM AM/PM)")
    
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "jpg", "png"])
    notes = st.text_area("Additional Notes")

    submitted = st.form_submit_button("Submit Offline Segment Request")

if submitted:
    st.success("✅ Offline segment request submitted.")
    # Add logic to save or pass data back to main ticket
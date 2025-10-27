import streamlit as st

st.title("🍽️ Move Break/Lunch Due to Meeting")

with st.form("move_segment_form"):
    segment_type = st.selectbox("What segment are we updating? *", ["Break", "Lunch"])
    new_start_time = st.text_input("New Start Time * (HH:MM AM/PM)")
    new_end_time = st.text_input("New End Time * (HH:MM AM/PM)")
    
    meeting_notes = st.text_area("Meeting Context or Notes")
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval (optional)", type=["pdf", "jpg", "png"])

    submitted = st.form_submit_button("Submit Segment Update")

if submitted:
    st.success("✅ Segment update submitted.")
    # Add logic to save or pass data back to main ticket
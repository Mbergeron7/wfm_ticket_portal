import streamlit as st
import datetime

st.title("🎓 Add / Remove / Move Training")

with st.form("training_form"):
    training_action = st.selectbox("What action are we performing? *", [
        "Add training", "Remove training", "Reschedule training"
    ])
    training_purpose = st.text_input("What is the training for? *")
    requested_date = st.date_input("Requested Date *", value=datetime.date.today())
    training_notes = st.text_area("Training Notes")
    
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "jpg", "png"])
    optional_notes = st.text_area("Optional Notes")

    submitted = st.form_submit_button("Submit Training Request")

if submitted:
    st.success("✅ Training request submitted.")
    # Add logic to save or pass data back to main ticket
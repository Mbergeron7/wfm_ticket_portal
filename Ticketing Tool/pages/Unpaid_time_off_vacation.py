import streamlit as st
import datetime

st.title("🌴 Unpaid Time Off / Vacation Request")

with st.form("unpaid_time_form"):
    start_date = st.date_input("Start Date *")
    end_date = st.date_input("End Date *")
    return_to_work = st.date_input("Return to Work Date *")

    # PeopleWare validation
    submitted_in_pw = st.radio("Request must be submitted in PeopleWare to be accepted *", ["Yes", "No"])
    st.markdown("📌 Days off must be booked in PeopleWare before sending approval to ensure processing.")

    # Uploads
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval (optional)", type=["pdf", "jpg", "png"])
    notes = st.text_area("Additional Notes (e.g. screenshots, IT ticket, context)")

    submitted = st.form_submit_button("Submit Time Off Request")

if submitted:
    st.success("✅ Time off request submitted.")
    # Add logic to save or pass data back to main ticket
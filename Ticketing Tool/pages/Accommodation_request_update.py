import streamlit as st
import datetime

st.title("🏠 Accommodation Request Form")

with st.form("accommodation_form"):
    start_date = st.date_input("Start Date *")
    end_date = st.date_input("End Date *")
    return_to_work = st.date_input("Return to Work Date *")
    accommodation_type = st.selectbox("Type of Accommodation *", ["School", "Personal", "Medical"])
    final_date = st.date_input("Final Date of Accommodation")
    school_schedule = st.file_uploader("📎 Upload School Schedule (optional)", type=["pdf", "docx", "xlsx", "jpg", "png"])
    
    # Weekly schedule
    st.markdown("### Weekly Schedule (HH:MM AM/PM)")
    monday = st.text_input("Monday")
    tuesday = st.text_input("Tuesday")
    wednesday = st.text_input("Wednesday")
    thursday = st.text_input("Thursday")
    friday = st.text_input("Friday")
    saturday = st.text_input("Saturday")
    sunday = st.text_input("Sunday")
    
    # CP3 approval
    cp3_approval = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "docx", "jpg", "png"])
    notes = st.text_area("Additional Notes")

    submitted = st.form_submit_button("Submit Accommodation Request")

if submitted:
    st.success("✅ Accommodation request submitted.")
    # You can add logic here to save to CSV or pass back to main ticket
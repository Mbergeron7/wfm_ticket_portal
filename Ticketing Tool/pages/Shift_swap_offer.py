import streamlit as st
import datetime

st.title("🔄 Shift Swap / Offer Request")

with st.form("shift_swap_form"):
    # Core fields already captured on main page
    swap_accepted_by = st.text_input("Advisor Accepting Swap *")
    offered_shift_date = st.date_input("Date of Offered Shift *")
    
    # PeopleWare validation
    submitted_in_pw = st.radio("Request submitted in PeopleWare? *", ["Yes", "No"])
    cp3_approval = st.radio("Approval by CP3? *", ["Yes", "No"])
    
    # Uploads
    pw_errors = st.file_uploader("📎 Upload screenshots of PeopleWare errors (both advisors)", type=["pdf", "jpg", "png"], accept_multiple_files=True)
    cp3_doc = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "jpg", "png"])
    
    # Notes
    notes = st.text_area("Additional Notes (e.g. IT ticket number, CP3 approval, context)")

    submitted = st.form_submit_button("Submit Shift Swap Request")

if submitted:
    st.success("✅ Shift swap request submitted.")
    # Add logic to save or pass data back to main ticket
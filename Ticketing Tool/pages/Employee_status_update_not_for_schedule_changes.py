import streamlit as st
import datetime

st.title("👤 Employee Status Update (Non-Schedule)")

with st.form("status_update_form"):
    status_type = st.selectbox("Type of Status Update *", [
        "Leave Type Change", "Role Change", "Return to Work", "Other"
    ])
    effective_date = st.date_input("Effective Date *", value=datetime.date.today())
    return_to_work = st.date_input("Return to Work Date (if applicable)")
    notes = st.text_area("Additional Notes (e.g. context, CP3 approval, IT ticket)")

    cp3_upload = st.file_uploader("📎 Upload CP3 Approval (optional)", type=["pdf", "jpg", "png"])

    submitted = st.form_submit_button("Submit Status Update")

if submitted:
    st.success("✅ Employee status update submitted.")
    # Add logic to save or pass data back to main ticket
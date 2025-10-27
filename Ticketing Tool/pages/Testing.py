import streamlit as st
import datetime

st.title("🧪 Testing Request")

with st.form("testing_form"):
    # Basic context
    feature_tested = st.text_input("What feature are you testing? *")
    test_date = st.date_input("Requested Date *", value=datetime.date.today())
    notes = st.text_area("Testing Notes / Observations")
    
    # Optional CP3 approval
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval (optional)", type=["pdf", "jpg", "png"])
    
    # Optional attachments
    attachments = st.file_uploader("📎 Upload Supporting Files (optional)", type=["pdf", "docx", "xlsx", "jpg", "png"], accept_multiple_files=True)

    submitted = st.form_submit_button("Submit Testing Request")

if submitted:
    st.success("✅ Testing request submitted.")
    # Add logic to save or pass data back to main ticket
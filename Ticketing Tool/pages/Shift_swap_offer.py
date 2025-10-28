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
    import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    r"C:\Users\mikeb\OneDrive - StorageVault Canada Inc\3.  Workforce Management\Mike Files\Power BI Files\Power Automate Schedule Files\Ticketing tool\Misc Files\credentials.json",
    scope
)
client = gspread.authorize(creds)
worksheet = client.open_by_key("1gzJ30wmAAcwEJ8H_nte7ZgH6suYZjGX_w86BhPIRndU").worksheet("Sheet1")

# Submit logic
if st.button("📨 Submit Ticket"):
    new_ticket = [
        f"TKT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
        advisor_name, team_lead, request_type, request_date.strftime("%Y-%m-%d"),
        priority, status, assigned_to, detail_1, detail_2, resolution_notes,
        datetime.datetime.now().isoformat()
    ]
    try:
        worksheet.append_row(new_ticket)
        st.success("✅ Ticket submitted to Google Sheets!")
    except Exception as e:
        st.error(f"❌ Submission failed: {e}")

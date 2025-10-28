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

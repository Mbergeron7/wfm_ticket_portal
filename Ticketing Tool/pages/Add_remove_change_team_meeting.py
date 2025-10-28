import streamlit as st
import datetime

st.title("📅 Add / Remove / Change Team Meeting")

with st.form("team_meeting_form"):
    meeting_action = st.selectbox("What are we updating for the meeting? *", [
        "Meeting End time", "Cancel Meeting", "Add Meeting"
    ])
    meeting_duration = st.number_input("How long is the meeting? (in minutes) *", min_value=1, max_value=999)
    inquiry_week = st.date_input("Which week are you inquiring for? (enter the Monday) *")
    notes = st.text_area("Additional Notes (e.g. CP3 approval, context)")

    submitted = st.form_submit_button("Submit Meeting Request")

if submitted:
    st.success("✅ Meeting request submitted.")

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

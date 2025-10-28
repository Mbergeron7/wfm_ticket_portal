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

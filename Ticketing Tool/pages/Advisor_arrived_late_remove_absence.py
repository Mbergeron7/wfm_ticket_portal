import streamlit as st

st.title("⏰ Advisor Arrived Late — Remove Absence")

with st.form("late_arrival_form"):
    # Old times
    st.markdown("### ⏪ Original Times")
    old_start_time = st.text_input("Old Start Time * (HH:MM AM/PM)")
    old_end_time = st.text_input("Old End Time * (HH:MM AM/PM)")

    # New times
    st.markdown("### ⏩ Corrected Times")
    new_start_time = st.text_input("New Start Time * (HH:MM AM/PM)")
    new_end_time = st.text_input("New End Time * (HH:MM AM/PM)")

    # Segment update
    segment_action = st.selectbox("Are we adding or removing a segment? *", ["Adding", "Removing"])
    segment_type = st.selectbox("Which segment is being updated? *", [
        "After Shift", "Client Account Work", "Coaching", "Code of Conduct", "Knowledge Assessment",
        "Leader on Duty", "Meeting", "Personal", "Spirit Committee", "System Issue", "System Outage"
    ])

    # CP3 approval
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "jpg", "png"])
    notes = st.text_area("Additional Notes")

    submitted = st.form_submit_button("Submit Absence Correction")

if submitted:
    st.success("✅ Absence correction submitted.")

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

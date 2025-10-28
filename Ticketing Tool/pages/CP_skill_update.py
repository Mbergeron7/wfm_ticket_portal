import streamlit as st

st.title("🧠 CP Skill Update")

with st.form("cp_skill_form"):
    skills_to_add = st.multiselect("Skill(s) to Add (max 2)", [
        "MoveBuddy", "PS CC EN", "PS CC FR", "PS Sales EN", "PS Sales FR", "PS Test",
        "PS WL EN", "PS WL FR", "SS CM EN", "SS CM FR", "SS Sales EN", "SS Sales FR",
        "SS Test", "SS WL EN", "SS WL FR"
    ], max_selections=2)

    skills_to_remove = st.multiselect("Skill(s) to Remove (max 2)", [
        "MoveBuddy", "PS CC EN", "PS CC FR", "PS Sales EN", "PS Sales FR", "PS Test",
        "PS WL EN", "PS WL FR", "SS CM EN", "SS CM FR", "SS Sales EN", "SS Sales FR",
        "SS Test", "SS WL EN", "SS WL FR"
    ], max_selections=2)

    cp_name_change = st.text_area("If a CP name change is also needed, please note it here.")
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "jpg", "png"])
    notes = st.text_area("Additional Notes")

    submitted = st.form_submit_button("Submit CP Skill Update")

if submitted:
    st.success("✅ CP skill update submitted.")

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

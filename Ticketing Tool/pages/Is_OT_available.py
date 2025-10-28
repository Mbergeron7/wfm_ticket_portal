import streamlit as st

st.title("🕒 Is Overtime Available?")

with st.form("ot_availability_form"):
    lob_assist = st.multiselect("Which LoB is the advisor looking to assist with for OT/additional hours? *", [
        "Admin", "ERO", "IT", "MoveBuddy", "PS BO", "PS CC", "PS CM", "PS Sales", "PS WL",
        "QA", "SS CM", "SS Sales", "SS WL", "TL/LoD"
    ])
    
    st.markdown("📌 If a skill update is required, please submit a separate form:")
    st.markdown("[🔗 Skill Update Form](https://forms.office.com/r/jzKwy84EMS)")
    
    notes = st.text_area("Additional Notes (e.g. context, CP3 approval, IT ticket)")

    submitted = st.form_submit_button("Submit OT Inquiry")

if submitted:
    st.success("✅ OT availability inquiry submitted.")

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

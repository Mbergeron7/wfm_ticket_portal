import streamlit as st
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# --- Google Sheets Setup ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    r"C:\Users\mikeb\OneDrive - StorageVault Canada Inc\3.  Workforce Management\Mike Files\Power BI Files\Power Automate Schedule Files\Ticketing tool\Misc Files\credentials.json",
    scope
)
client = gspread.authorize(creds)
worksheet = client.open_by_key("1gzJ30wmAAcwEJ8H_nte7ZgH6suYZjGX_w86BhPIRndU").worksheet("Sheet1")

# --- UI ---
st.set_page_config(page_title="Testing Request", page_icon="🧪")
st.title("🧪 Submit a Testing Request")

with st.form("testing_form"):
    feature_tested = st.text_input("What feature are you testing? *")
    test_date = st.date_input("Requested Date *", value=datetime.date.today())
    notes = st.text_area("Testing Notes / Observations")

    cp3_upload = st.file_uploader("📎 Upload CP3 Approval (optional)", type=["pdf", "jpg", "png"])
    attachments = st.file_uploader("📎 Upload Supporting Files (optional)", type=["pdf", "docx", "xlsx", "jpg", "png"], accept_multiple_files=True)

    submitted = st.form_submit_button("📨 Submit Testing Request")

# --- Submission Logic ---
if submitted:
    if feature_tested:
        new_ticket = [
            f"TKT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",  # Ticket ID
            "Testing",  # Advisor Name
            "System",   # Team Lead
            "Testing Request",  # Request Type
            test_date.strftime("%Y-%m-%d"),  # Request Date
            "Low",  # Priority
            "Open",  # Status
            "Mike Bergeron",  # Assigned To
            feature_tested,  # Detail 1
            notes,           # Detail 2
            "",              # Resolution Notes
            datetime.datetime.now().isoformat()  # Created Timestamp
        ]
        try:
            worksheet.append_row(new_ticket)
            st.success("✅ Testing request submitted to Google Sheets!")
        except Exception as e:
            st.error(f"❌ Submission failed: {e}")
    else:
        st.warning("⚠️ Please enter the feature being tested.")

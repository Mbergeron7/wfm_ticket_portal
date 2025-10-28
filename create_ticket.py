import streamlit as st
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# --- Google Sheets Setup ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1gzJ30wmAAcwEJ8H_nte7ZgH6suYZjGX_w86BhPIRndU").sheet1

# --- Streamlit UI ---
st.set_page_config(page_title="Create Ticket", page_icon="🎫")
st.title("🎫 Submit a New Ticket")

advisor_name = st.text_input("Advisor Name *")
team_lead = st.selectbox("Team Lead *", [
    "Select...", "Adeyinka", "Alana", "Alexandra", "Aman", "Bryan", "Cushana", "David", "Dee", "Jodi", "Julianne",
    "Kristin", "Lucas", "Maggie", "Mike", "Odette", "Pat", "Salomon", "Sean", "Shavindri", "Teresa"
])
request_type = st.selectbox("Request Type *", [
    "Select...", "Accommodation request/update", "Add additional hours", "Add/remove/change team meeting",
    "Add/remove/move training", "Add offline segment", "Advisor arrived late, remove absence",
    "CP skill update", "Employee status update (not for schedule changes)", "Is OT available?",
    "Move break/lunch because of meeting", "Schedule Update - CP3 use", "Schedule Error Adjustment",
    "Shift swap/offer", "Suggestions/Feedback", "Unpaid time off/vacation", "Testing"
])
request_date = st.date_input("Request Date", value=datetime.date.today())
priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
assigned_to = st.selectbox("Assigned To *", ["Select...", "Mike Bergeron", "Dawn Devenny", "Josh Sauve", "JC Ilunga"])
detail_1 = st.text_area("Details (Part 1)")
detail_2 = st.text_area("Details (Part 2)")
resolution_notes = st.text_area("Resolution Notes")

# --- Submission Logic ---
if st.button("📨 Submit Ticket"):
    if advisor_name and team_lead != "Select..." and request_type != "Select..." and assigned_to != "Select...":
        new_ticket = [
            f"TKT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
            advisor_name, team_lead, request_type, request_date.strftime("%Y-%m-%d"),
            priority, status, assigned_to, detail_1, detail_2, resolution_notes,
            datetime.datetime.now().isoformat()
        ]
        try:
            sheet.append_row(new_ticket)
            st.success("✅ Ticket submitted to Google Sheets!")
            st.dataframe([new_ticket], use_container_width=True)
        except Exception as e:
            st.error(f"❌ Failed to submit ticket: {e}")
    else:
        st.warning("⚠️ Please complete all required fields marked with *")

# --- Footer ---
st.markdown("---")
st.caption("This ticket is saved to a cloud-based Google Sheet. Accessible to all authorized team members.")


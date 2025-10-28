import streamlit as st
import pandas as pd
import datetime
import os

# Path to synced SharePoint file
TICKET_PATH = r"C:\Users\mikeb\OneDrive - StorageVault Canada Inc\3.  Workforce Management\Mike Files\Power BI Files\Power Automate Schedule Files\Ticketing Tool\incoming_tickets.csv"

st.title("🎫 Create New Ticket")

# Core fields
advisor_name = st.text_input("Advisor Name *")

team_lead = st.selectbox("Advisor Team Lead *", [
    "Select...", "Adeyinka", "Alana", "Alexandra", "Aman", "Bryan", "Cushana", "David", "Dee", "Jodi", "Julianne",
    "Kristin", "Lucas", "Maggie", "Mike", "Odette", "Pat", "Salomon", "Sean", "Shavindri", "Teresa"
])

request_date = st.date_input("Date for Request *", value=datetime.date.today())

request_type = st.selectbox("WFM Request *", [
    "Select...", "Accommodation request/update", "Add additional hours", "Add/remove/change team meeting",
    "Add/remove/move training", "Add offline segment", "Advisor arrived late, remove absence",
    "CP skill update", "Employee status update (not for schedule changes)", "Is OT available?",
    "Move break/lunch because of meeting", "Schedule Update - CP3 use", "Schedule Error Adjustment",
    "Shift swap/offer", "Suggestions/Feedback", "Unpaid time off/vacation", "Testing"
])

detail_1 = st.text_area("Detail (Part 1)")
detail_2 = st.text_area("Detail (Part 2)")

priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Escalated"])

assigned_to = st.selectbox("Assigned To", [
    "Select...", "Mike Bergeron", "Dawn Devenny", "Josh Sauve", "JC Ilunga"
])

resolution_notes = st.text_area("Resolution Notes")

# Submit button
if st.button("📨 Submit Ticket"):
    if advisor_name and team_lead != "Select..." and request_type != "Select..." and assigned_to != "Select...":
        new_ticket = {
            "Ticket ID": f"TKT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
            "Advisor Name": advisor_name,
            "Team Lead": team_lead,
            "Request Date": request_date.strftime("%Y-%m-%d"),
            "Request Type": request_type,
            "Detail 1": detail_1,
            "Detail 2": detail_2,
            "Priority": priority,
            "Status": status,
            "Assigned To": assigned_to,
            "Resolution Notes": resolution_notes,
            "Created Timestamp": datetime.datetime.now().isoformat()
        }

        try:
            if os.path.exists(TICKET_PATH):
                df = pd.read_csv(TICKET_PATH)
                df = pd.concat([df, pd.DataFrame([new_ticket])], ignore_index=True)
            else:
                df = pd.DataFrame([new_ticket])

            df.to_csv(TICKET_PATH, index=False)
            st.success("✅ Ticket submitted and saved to SharePoint!")
        except Exception as e:
            st.error(f"❌ Failed to save ticket: {e}")
    else:
        st.warning("Please complete all required fields marked with *")

# 🔗 Link to selected request form
if request_type and request_type != "Select...":
    page_name = request_type.replace(" ", "_").replace("/", "_")
    st.markdown(f"[➡️ Continue to {request_type} Form]({page_name})")

# 🧭 Link to full request list
st.markdown("---")

st.markdown("[📋 View All Request Types](Request_Categories)")

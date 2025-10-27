import streamlit as st
import datetime

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

# 🔗 Link to selected request form
if request_type and request_type != "Select...":
    page_name = request_type.replace(" ", "_").replace("/", "_")
    st.markdown(f"[➡️ Continue to {request_type} Form]({page_name})")

# 🧭 Link to full request list
st.markdown("---")
st.markdown("[📋 View All Request Types](Request_Categories)")





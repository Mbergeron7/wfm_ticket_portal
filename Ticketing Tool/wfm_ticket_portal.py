import streamlit as st
import pandas as pd
import uuid
import datetime
import os

CSV_PATH = "WFM_Tickets_backup.csv"

st.title("🎫 WFM Ticket Portal")

# 🔗 Dashboard link (matches pages/Ticket_Dashboard.py)
st.markdown("[📊 Open Dashboard](Ticket_Dashboard)")

# ✅ Detect query param for ticket drill-down
selected_id = st.query_params.get("ticket_id", None)

# 🔍 If ticket_id is passed, show ticket details and edit panel
if selected_id:
    st.subheader(f"🔍 Ticket Details: {selected_id}")
    
    if not os.path.exists(CSV_PATH):
        st.error("Ticket data not found.")
        st.stop()

    df = pd.read_csv(CSV_PATH)
    if selected_id not in df["ticket_id"].values:
        st.error("Ticket ID not found.")
        st.stop()

    ticket = df[df["ticket_id"] == selected_id].iloc[0]

    # Display all ticket fields
    for key, value in ticket.items():
        st.write(f"**{key}**: {value}")

    # Editable fields
    st.markdown("### 🛠️ Work Ticket")
    new_status = st.selectbox("Update Status", [" ", "Open", "In Progress", "Resolved", "Escalated"], index=["Open", "In Progress", "Resolved", "Escalated"].index(ticket["status"]))
    new_notes = st.text_area("Resolution Notes", value=ticket.get("resolution_notes", ""))
    new_assigned = st.text_input("Reassign To", value=ticket.get("assigned_to", ""))

    if st.button("💾 Save Changes"):
        now = datetime.datetime.now(datetime.UTC).isoformat()
        df.loc[df["ticket_id"] == selected_id, "status"] = new_status
        df.loc[df["ticket_id"] == selected_id, "resolution_notes"] = new_notes
        df.loc[df["ticket_id"] == selected_id, "assigned_to"] = new_assigned
        df.loc[df["ticket_id"] == selected_id, "last_updated"] = now
        df.to_csv(CSV_PATH, index=False)
        st.toast("✅ Ticket updated")
        st.rerun()

    st.markdown("[← Back to Dashboard](Ticket_Dashboard)")
    st.stop()

# 📝 Ticket submission form
st.subheader("Create New Ticket")

with st.form("ticket_form"):
    advisor_name = st.text_input("Advisor Name *")
    team_lead = st.selectbox("Advisor Team Lead *", [" ", "Adeyinka", "Alana", "Alexandra", "Aman", "Bryan", "Cushana", "David", "Dee", "Jodi", "Julianne", "Kristin", "Lucas", "Maggie", "Mike", "Odette", "Pat", "Salomon", "Sean", "Shavindri", "Teresa"])
    request_date = st.date_input("Date for Request *", value=datetime.date.today())
    request_type = st.selectbox("WFM Request *", ["Accommodation request/update", "Add additional hours", "Add/remove/change team meeting", "Add/remove/move training", "Add offline segment", "Advisor arrived late, remove absence", "CP skill update", "Employee status update (not for schedule changes)", "Is OT available?", "Move break/lunch because of meeting", "Schedule Update - CP3 use", "Schedule Error Adjustment", "Shift swap/offer", "Suggestions/Feedback", "Unpaid time off/vacation", "Testing"])
    detail_1 = st.text_area("Detail (Part 1)")
    detail_2 = st.text_area("Detail (Part 2)")
    priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
    status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Escalated"])
    assigned_to = st.text_input("Assigned To", value="wfm_analyst_1")
    resolution_notes = st.text_area("Resolution Notes")
    submitted = st.form_submit_button("Submit Ticket")

# 💾 Save new ticket
if submitted:
    now = datetime.datetime.now(datetime.UTC).isoformat()
    ticket = {
        "ticket_id": str(uuid.uuid4()),
        "created_at": now,
        "last_updated": now,
        "advisor_name": advisor_name,
        "team_lead": team_lead,
        "request_date": request_date.isoformat(),
        "request_type": request_type,
        "detail_1": detail_1,
        "detail_2": detail_2,
        "priority": priority,
        "status": status,
        "assigned_to": assigned_to,
        "resolution_notes": resolution_notes
    }

    df = pd.DataFrame([ticket])
    if os.path.exists(CSV_PATH):
        df.to_csv(CSV_PATH, mode='a', header=False, index=False)
    else:
        df.to_csv(CSV_PATH, index=False)

    st.success(f"✅ Ticket submitted: {ticket['ticket_id']}")


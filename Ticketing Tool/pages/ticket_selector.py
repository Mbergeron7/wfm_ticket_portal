import streamlit as st
import pandas as pd
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

# --- Load ticket data ---
def load_tickets():
    try:
        records = worksheet.get_all_records()
        df = pd.DataFrame(records)
        return df
    except Exception as e:
        st.error(f"❌ Failed to load tickets: {e}")
        return pd.DataFrame()

tickets = load_tickets()

# --- Sidebar filters ---
st.set_page_config(page_title="Ticket Selector", page_icon="📥")
st.sidebar.header("🔍 Filter Tickets")

status_options = tickets["Status"].dropna().unique()
team_options = tickets["Team Lead"].dropna().unique()
priority_options = tickets["Priority"].dropna().unique()

selected_status = st.sidebar.multiselect("Status", options=status_options)
selected_team = st.sidebar.multiselect("Team Lead", options=team_options)
selected_priority = st.sidebar.multiselect("Priority", options=priority_options)

# --- Apply filters ---
filtered = tickets.copy()
if selected_status:
    filtered = filtered[filtered["Status"].isin(selected_status)]
if selected_team:
    filtered = filtered[filtered["Team Lead"].isin(selected_team)]
if selected_priority:
    filtered = filtered[filtered["Priority"].isin(selected_priority)]

# --- Main dashboard ---
st.title("📥 Incoming Ticket Selector")
st.write(f"Showing **{len(filtered)}** tickets")

if len(filtered) == 0:
    st.info("No tickets match the selected filters.")
else:
    ticket_ids = filtered["Ticket ID"].dropna().unique()
    selected_ticket = st.selectbox("Select a ticket", ticket_ids)

    ticket_details = filtered[filtered["Ticket ID"] == selected_ticket].iloc[0]
    with st.expander("📄 Ticket Details"):
        st.markdown(f"**Advisor Name:** {ticket_details['Advisor Name']}")
        st.markdown(f"**Team Lead:** {ticket_details['Team Lead']}")
        st.markdown(f"**Request Type:** {ticket_details['Request Type']}")
        st.markdown(f"**Request Date:** {ticket_details['Request Date']}")
        st.markdown(f"**Priority:** {ticket_details['Priority']}")
        st.markdown(f"**Status:** {ticket_details['Status']}")
        st.markdown(f"**Assigned To:** {ticket_details['Assigned To']}")
        st.markdown(f"**Detail 1:**\n{ticket_details['Detail 1']}")
        st.markdown(f"**Detail 2:**\n{ticket_details['Detail 2']}")
        st.markdown(f"**Resolution Notes:**\n{ticket_details['Resolution Notes']}")
        st.markdown(f"**Created Timestamp:** {ticket_details['Created Timestamp']}")

    # --- Action buttons ---
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Assign Ticket"):
            st.success("Ticket assigned!")  # Add update logic if needed
    with col2:
        if st.button("🚨 Escalate Ticket"):
            st.warning("Ticket escalated!")  # Add escalation logic if needed

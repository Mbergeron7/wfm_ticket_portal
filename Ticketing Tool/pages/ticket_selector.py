import streamlit as st
import pandas as pd
import os

# Local path to synced SharePoint CSV
TICKET_PATH = r"C:\Users\mikeb\OneDrive - StorageVault Canada Inc\3.  Workforce Management\Mike Files\Power BI Files\Power Automate Schedule Files\Ticketing Tool\incoming_tickets.csv"

# Load ticket data
@st.cache_data
def load_tickets():
    if os.path.exists(TICKET_PATH):
        df = pd.read_csv(TICKET_PATH)
        return df
    else:
        st.error("❌ Ticket file not found at expected path.")
        return pd.DataFrame()

tickets = load_tickets()

# Sidebar filters
st.sidebar.header("🔍 Filter Tickets")
status_options = tickets["Status"].dropna().unique()
team_options = tickets["Team Lead"].dropna().unique()
priority_options = tickets["Priority"].dropna().unique()

selected_status = st.sidebar.multiselect("Status", options=status_options)
selected_team = st.sidebar.multiselect("Team Lead", options=team_options)
selected_priority = st.sidebar.multiselect("Priority", options=priority_options)

# Apply filters
filtered = tickets.copy()
if selected_status:
    filtered = filtered[filtered["Status"].isin(selected_status)]
if selected_team:
    filtered = filtered[filtered["Team Lead"].isin(selected_team)]
if selected_priority:
    filtered = filtered[filtered["Priority"].isin(selected_priority)]

# Main dashboard
st.title("📥 Incoming Ticket Selector")
st.write(f"Showing **{len(filtered)}** tickets")

# Ticket selection
ticket_ids = filtered["Ticket ID"].dropna().unique()
selected_ticket = st.selectbox("Select a ticket", ticket_ids)

# Show ticket details
ticket_details = filtered[filtered["Ticket ID"] == selected_ticket].iloc[0]
with st.expander("📄 Ticket Details"):
    st.markdown(f"**Subject:** {ticket_details['Subject']}")
    st.markdown(f"**Created:** {ticket_details['Created Date']}")
    st.markdown(f"**Team Lead:** {ticket_details['Team']}")
    st.markdown(f"**Priority:** {ticket_details['Priority']}")
    st.markdown(f"**Status:** {ticket_details['Status']}")
    st.markdown(f"**SLA Risk:** {ticket_details['SLA Risk']}")
    st.markdown(f"**Description:**\n{ticket_details['Description']}")

# Action buttons
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Assign Ticket"):
        st.success("Ticket assigned!")  # You can add logic to update the CSV here
with col2:
    if st.button("🚨 Escalate Ticket"):
        st.warning("Ticket escalated!")  # Same here for escalation logic






import streamlit as st
import pandas as pd
import os

# Load ticket data from synced SharePoint file
@st.cache_data
def load_tickets():
    file_path = os.path.expanduser("~/OneDrive - StorageVault Canada Inc/BusinessIntelligence/incoming_tickets.csv")
    df = pd.read_csv(file_path)
    return df

tickets = load_tickets()

# Sidebar filters
st.sidebar.header("🔍 Filter Tickets")
status_options = tickets["Status"].dropna().unique()
team_options = tickets["Team"].dropna().unique()
priority_options = tickets["Priority"].dropna().unique()

selected_status = st.sidebar.multiselect("Status", options=status_options)
selected_team = st.sidebar.multiselect("Team", options=team_options)
selected_priority = st.sidebar.multiselect("Priority", options=priority_options)

# Apply filters
filtered = tickets.copy()
if selected_status:
    filtered = filtered[filtered["Status"].isin(selected_status)]
if selected_team:
    filtered = filtered[filtered["Team"].isin(selected_team)]
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
    st.markdown(f"**Team:** {ticket_details['Team']}")
    st.markdown(f"**Priority:** {ticket_details['Priority']}")
    st.markdown(f"**Status:** {ticket_details['Status']}")
    st.markdown(f"**SLA Risk:** {ticket_details['SLA Risk']}")
    st.markdown(f"**Description:**\n{ticket_details['Description']}")

# Action buttons
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Assign Ticket"):
        st.success("Ticket assigned!")
with col2:
    if st.button("🚨 Escalate Ticket"):
        st.warning("Ticket escalated!")

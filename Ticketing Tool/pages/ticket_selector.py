import streamlit as st
import pandas as pd

# Load ticket data
@st.cache_data
def load_tickets():
    df = pd.read_csv("incoming_tickets.csv")  # Replace with your actual source
    return df

tickets = load_tickets()

# Sidebar filters
st.sidebar.header("Filter Tickets")
selected_status = st.sidebar.multiselect("Status", options=tickets["Status"].unique())
selected_team = st.sidebar.multiselect("Team", options=tickets["Team"].unique())
selected_priority = st.sidebar.multiselect("Priority", options=tickets["Priority"].unique())

# Apply filters
filtered = tickets.copy()
if selected_status:
    filtered = filtered[filtered["Status"].isin(selected_status)]
if selected_team:
    filtered = filtered[filtered["Team"].isin(selected_team)]
if selected_priority:
    filtered = filtered[filtered["Priority"].isin(selected_priority)]

# Main dashboard
st.title("🎫 Incoming Ticket Selector")
st.write(f"Showing {len(filtered)} tickets")

# Display ticket table
selected_ticket = st.selectbox("Select a ticket", filtered["Ticket ID"])

# Show details
ticket_details = filtered[filtered["Ticket ID"] == selected_ticket].iloc[0]
with st.expander("Ticket Details"):
    st.write(f"**Subject:** {ticket_details['Subject']}")
    st.write(f"**Created:** {ticket_details['Created Date']}")
    st.write(f"**Team:** {ticket_details['Team']}")
    st.write(f"**Priority:** {ticket_details['Priority']}")
    st.write(f"**Status:** {ticket_details['Status']}")
    st.write(f"**SLA Risk:** {ticket_details['SLA Risk']}")
    st.write(f"**Description:**\n{ticket_details['Description']}")

# Optional action buttons
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Assign Ticket"):
        st.success("Ticket assigned!")
with col2:
    if st.button("🚨 Escalate Ticket"):
        st.warning("Ticket escalated!")

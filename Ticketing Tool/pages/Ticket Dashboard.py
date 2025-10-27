import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📊 Ticket Dashboard", layout="wide")
st.title("📊 WFM Ticket Dashboard")

# 🔄 Load ticket data
TICKET_FILE = "tickets.csv"  # Update path if needed

if os.path.exists(TICKET_FILE):
    df = pd.read_csv(TICKET_FILE)
else:
    st.warning("No ticket data found.")
    st.stop()

# 🧭 Sidebar filters
st.sidebar.header("🔍 Filter Tickets")
request_types = df["WFM Request"].dropna().unique()
team_leads = df["Advisor Team Lead"].dropna().unique()
status_options = df["Status"].dropna().unique()

selected_type = st.sidebar.multiselect("Request Type", request_types)
selected_lead = st.sidebar.multiselect("Team Lead", team_leads)
selected_status = st.sidebar.multiselect("Status", status_options)

# 🧮 Apply filters
filtered_df = df.copy()
if selected_type:
    filtered_df = filtered_df[filtered_df["WFM Request"].isin(selected_type)]
if selected_lead:
    filtered_df = filtered_df[filtered_df["Advisor Team Lead"].isin(selected_lead)]
if selected_status:
    filtered_df = filtered_df[filtered_df["Status"].isin(selected_status)]

# 📋 Display table
st.markdown("### 🎟️ Filtered Tickets")
st.dataframe(filtered_df, use_container_width=True)

# 📊 Summary metrics
st.markdown("### 📈 Ticket Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Tickets", len(df))
col2.metric("Open Tickets", (df["Status"] == "Open").sum())
col3.metric("Resolved Tickets", (df["Status"] == "Resolved").sum())

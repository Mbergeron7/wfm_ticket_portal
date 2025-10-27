import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
import plotly.express as px

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

# ✅ Export filtered tickets to CSV
st.download_button(
    label="📥 Export Filtered Tickets to CSV",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_tickets.csv",
    mime="text/csv"
)

# ✅ Highlight overdue or high-priority tickets
if "Date for Request" in df.columns and "Priority" in df.columns:
    filtered_df["Overdue"] = pd.to_datetime(filtered_df["Date for Request"], errors="coerce") < datetime.today() - timedelta(days=7)
    filtered_df["High Priority"] = filtered_df["Priority"].str.lower() == "high"

    def highlight_flags(row):
        color = ""
        if row.get("Overdue"):
            color = "background-color: #ffcccc"
        elif row.get("High Priority"):
            color = "background-color: #fff3cd"
        return [color] * len(row)

    st.markdown("### 🎯 Highlighted Tickets")
    st.dataframe(filtered_df.style.apply(highlight_flags, axis=1), use_container_width=True)
else:
    st.markdown("### 🎯 Filtered Tickets")
    st.dataframe(filtered_df, use_container_width=True)

# ✅ Add edit or comment functionality
st.markdown("### 📝 Add Comments to a Ticket")

if "Comment" not in df.columns:
    df["Comment"] = ""

ticket_ids = filtered_df.index.tolist()
if ticket_ids:
    selected_ticket = st.selectbox("Select Ticket ID", ticket_ids)
    current_comment = df.loc[selected_ticket, "Comment"]
    comment = st.text_area("Add or Edit Comment", value=current_comment)

    if st.button("Save Comment"):
        df.loc[selected_ticket, "Comment"] = comment
        df.to_csv(TICKET_FILE, index=False)
        st.success("✅ Comment saved.")
else:
    st.info("No tickets available to comment on.")

# ✅ Embed charts
st.markdown("### 📊 Ticket Volume by Request Type")
type_chart = px.bar(df["WFM Request"].value_counts().reset_index(),
                    x="index", y="WFM Request",
                    labels={"index": "Request Type", "WFM Request": "Count"},
                    title="Tickets by Request Type")
st.plotly_chart(type_chart, use_container_width=True)

st.markdown("### 📊 Ticket Volume by Team Lead")
lead_chart = px.pie(df, names="Advisor Team Lead", title="Tickets by Team Lead")
st.plotly_chart(lead_chart, use_container_width=True)

# ✅ Summary metrics
st.markdown("### 📈 Ticket Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Tickets", len(df))
col2.metric("Open Tickets", (df["Status"] == "Open").sum())
col3.metric("Resolved Tickets", (df["Status"] == "Resolved").sum())

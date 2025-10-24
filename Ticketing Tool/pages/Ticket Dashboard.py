import streamlit as st
import pandas as pd
import datetime
import os
from st_aggrid import AgGrid, GridOptionsBuilder

CSV_PATH = "WFM_Tickets_backup.csv"

st.title("📊 WFM Ticket Dashboard")

# 🔗 Link back to main ticket submission page
st.markdown("[➕ Create New Ticket](wfm_ticket_portal)")

# 🚨 Check for data
if not os.path.exists(CSV_PATH):
    st.warning("No ticket data found.")
    st.stop()

# 📥 Load and process data
df = pd.read_csv(CSV_PATH)
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
df["last_updated"] = pd.to_datetime(df["last_updated"], errors="coerce")
now = datetime.datetime.now(datetime.UTC)
df["ticket_age_hours"] = (now - df["created_at"]).dt.total_seconds() / 3600
df["sla_breach"] = (df["ticket_age_hours"] > 48) & (df["status"] != "Resolved")

# 🧠 Risk scoring
def risk_score(row):
    score = 0
    if row["priority"] == "Critical":
        score += 40
    elif row["priority"] == "High":
        score += 30
    elif row["priority"] == "Medium":
        score += 20
    score += min(row["ticket_age_hours"], 48) / 2
    if row["status"] == "Escalated":
        score += 20
    return min(score, 100)

df["risk_score"] = df.apply(risk_score, axis=1)

# 📈 Advisor performance
st.subheader("📈 Advisor Performance")
perf_df = df.copy()
perf_df["resolution_time"] = (perf_df["last_updated"] - perf_df["created_at"]).dt.total_seconds() / 3600
advisor_perf = perf_df.groupby("advisor_name").agg({
    "ticket_id": "count",
    "resolution_time": "mean",
    "sla_breach": "sum",
    "risk_score": "mean"
}).reset_index()
advisor_perf.columns = ["Advisor", "Ticket Count", "Avg Resolution (hrs)", "SLA Breaches", "Avg Risk Score"]
st.dataframe(advisor_perf.sort_values("Avg Risk Score", ascending=False), use_container_width=True)

# 🔍 High-risk filter
st.subheader("🧠 High-Risk Tickets")
high_risk = df[df["risk_score"] > 70]
if not high_risk.empty:
    st.warning(f"{high_risk.shape[0]} high-risk ticket(s) detected.")
    st.dataframe(high_risk[["ticket_id", "advisor_name", "priority", "status", "risk_score"]], use_container_width=True)

# 📋 Drill-down table with clickable ticket links
st.subheader("🔍 All Tickets")

# Create clickable links using query params
df["ticket_link"] = df["ticket_id"].apply(lambda tid: f"[{tid}](wfm_ticket_portal?ticket_id={tid})")
display_df = df[["ticket_link", "advisor_name", "priority", "status", "risk_score", "sla_breach", "created_at", "last_updated"]]
display_df.rename(columns={"ticket_link": "Ticket ID"}, inplace=True)

gb = GridOptionsBuilder.from_dataframe(display_df)
gb.configure_column("sla_breach", cellStyle={"color": "red"}, header_name="SLA Breach")
gb.configure_column("risk_score", type=["numericColumn"], header_name="Risk Score")
gb.configure_selection("single", use_checkbox=True)
grid_options = gb.build()

AgGrid(display_df, gridOptions=grid_options, height=400, theme="streamlit")

# 📤 Export
st.subheader("📤 Export")
st.download_button(
    label="Download All Tickets as CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="wfm_tickets_full.csv",
    mime="text/csv"
)

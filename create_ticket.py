import streamlit as st
import pandas as pd
import datetime
import os

# ✅ Confirmed local path to shared OneDrive CSV
TICKET_PATH = r"C:\Users\mikeb\OneDrive - StorageVault Canada Inc\3.  Workforce Management\Mike Files\Power BI Files\Power Automate Schedule Files\Ticketing Tool\incoming_tickets.csv"

st.set_page_config(page_title="Create Ticket", page_icon="🎫")
st.title("🎫 Create New Ticket")

# --- Form Inputs ---
advisor_name = st.text_input("Advisor Name *")
team_lead = st.selectbox("Team Lead *", ["Select...", "Mike", "Odette", "Teresa", "Sean"])
request_type = st.selectbox("Request Type *", ["Select...", "Schedule Update", "Shift Swap", "Training Request"])
request_date = st.date_input("Request Date", value=datetime.date.today())
priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
assigned_to = st.selectbox("Assigned To *", ["Select...", "Mike Bergeron", "Dawn Devenny", "Josh Sauve", "JC Ilunga"])
detail_1 = st.text_area("Details (Part 1)")
detail_2 = st.text_area("Details (Part 2)")
resolution_notes = st.text_area("Resolution Notes")

# --- Submission Logic ---
if st.button("📨 Submit Ticket"):
    # Validate required fields
    if advisor_name and team_lead != "Select..." and request_type != "Select..." and assigned_to != "Select...":
        new_ticket = {
            "Ticket ID": f"TKT-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
            "Advisor Name": advisor_name,
            "Team Lead": team_lead,
            "Request Type": request_type,
            "Request Date": request_date.strftime("%Y-%m-%d"),
            "Priority": priority,
            "Status": status,
            "Assigned To": assigned_to,
            "Detail 1": detail_1,
            "Detail 2": detail_2,
            "Resolution Notes": resolution_notes,
            "Created Timestamp": datetime.datetime.now().isoformat()
        }

        try:
            # Load existing CSV or create new
            if os.path.exists(TICKET_PATH):
                df = pd.read_csv(TICKET_PATH)
                df = pd.concat([df, pd.DataFrame([new_ticket])], ignore_index=True)
            else:
                df = pd.DataFrame([new_ticket])

            # Write to CSV
            df.to_csv(TICKET_PATH, index=False)
            st.success("✅ Ticket submitted and saved to shared OneDrive!")
            st.text(f"Saved to: {TICKET_PATH}")
        except PermissionError:
            st.error("❌ File is locked. Please close it in Excel and try again.")
        except Exception as e:
            st.error(f"❌ Failed to save ticket: {e}")
    else:
        st.warning("⚠️ Please complete all required fields marked with *")

# --- Footer ---
st.markdown("---")
st.caption("This ticket will be synced to SharePoint via OneDrive. Ensure the file is not open in Excel during submission.")


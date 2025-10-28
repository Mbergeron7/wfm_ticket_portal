import streamlit as st
import pandas as pd
import datetime
import os

# ✅ Confirmed path to shared OneDrive CSV
TICKET_PATH = r"C:\Users\mikeb\OneDrive - StorageVault Canada Inc\3.  Workforce Management\Mike Files\Power BI Files\Power Automate Schedule Files\Ticketing Tool\incoming_tickets.csv"

# ✅ Define expected schema
expected_columns = [
    "Ticket ID", "Advisor Name", "Team Lead", "Request Type", "Request Date",
    "Priority", "Status", "Assigned To", "Detail 1", "Detail 2",
    "Resolution Notes", "Created Timestamp"
]

# ✅ Ensure CSV exists and has correct columns
if not os.path.exists(TICKET_PATH) or os.path.getsize(TICKET_PATH) == 0:
    df_init = pd.DataFrame(columns=expected_columns)
    df_init.to_csv(TICKET_PATH, index=False)
else:
    try:
        df_existing = pd.read_csv(TICKET_PATH)
        missing_cols = [col for col in expected_columns if col not in df_existing.columns]
        if missing_cols:
            for col in missing_cols:
                df_existing[col] = ""
            df_existing = df_existing[expected_columns]
            df_existing.to_csv(TICKET_PATH, index=False)
    except Exception as e:
        st.error(f"❌ Failed to validate CSV schema: {e}")

# --- Streamlit UI ---
st.set_page_config(page_title="Create Ticket", page_icon="🎫")
st.title("🎫 Submit a New Ticket")

advisor_name = st.text_input("Advisor Name *")
team_lead = st.selectbox("Team Lead *", [
    "Select...", "Adeyinka", "Alana", "Alexandra", "Aman", "Bryan", "Cushana", "David", "Dee", "Jodi", "Julianne",
    "Kristin", "Lucas", "Maggie", "Mike", "Odette", "Pat", "Salomon", "Sean", "Shavindri", "Teresa"
])
request_type = st.selectbox("Request Type *", [
    "Select...", "Accommodation request/update", "Add additional hours", "Add/remove/change team meeting",
    "Add/remove/move training", "Add offline segment", "Advisor arrived late, remove absence",
    "CP skill update", "Employee status update (not for schedule changes)", "Is OT available?",
    "Move break/lunch because of meeting", "Schedule Update - CP3 use", "Schedule Error Adjustment",
    "Shift swap/offer", "Suggestions/Feedback", "Unpaid time off/vacation", "Testing"
])
request_date = st.date_input("Request Date", value=datetime.date.today())
priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])
assigned_to = st.selectbox("Assigned To *", ["Select...", "Mike Bergeron", "Dawn Devenny", "Josh Sauve", "JC Ilunga"])
detail_1 = st.text_area("Details (Part 1)")
detail_2 = st.text_area("Details (Part 2)")
resolution_notes = st.text_area("Resolution Notes")

# --- Submission Logic ---
if st.button("📨 Submit Ticket"):
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
            df = pd.read_csv(TICKET_PATH)
            df = pd.concat([df, pd.DataFrame([new_ticket])], ignore_index=True)
            df.to_csv(TICKET_PATH, index=False)
            st.success("✅ Ticket submitted successfully!")
            st.text(f"Saved to: {TICKET_PATH}")
        except PermissionError:
            st.error("❌ File is locked. Please close it in Excel and try again.")
        except Exception as e:
            st.error(f"❌ Failed to save ticket: {e}")
    else:
        st.warning("⚠️ Please complete all required fields marked with *")

# --- Footer ---
st.markdown("---")
st.caption("This ticket is saved to a shared OneDrive folder and synced to SharePoint. Ensure the file is not open in Excel during submission.")




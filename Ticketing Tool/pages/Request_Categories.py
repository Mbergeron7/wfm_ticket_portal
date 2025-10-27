import streamlit as st

st.title("📋 All WFM Request Types")

request_types = [
    "Accommodation request/update", "Add additional hours", "Add/remove/change team meeting",
    "Add/remove/move training", "Add offline segment", "Advisor arrived late, remove absence",
    "CP skill update", "Employee status update (not for schedule changes)", "Is OT available?",
    "Move break/lunch because of meeting", "Schedule Update - CP3 use", "Schedule Error Adjustment",
    "Shift swap/offer", "Suggestions/Feedback", "Unpaid time off/vacation", "Testing"
]

for req in request_types:
    page_name = req.replace(" ", "_").replace("/", "_")
    st.markdown(f"- [📝 {req}]({page_name})")
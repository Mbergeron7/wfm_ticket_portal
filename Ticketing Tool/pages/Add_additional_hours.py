import streamlit as st
import datetime

st.title("⏱️ Add Additional Hours Request")

with st.form("additional_hours_form"):
    # Core fields already captured on main page
    num_days = st.selectbox("How many days are we adding additional hours to? *", ["1 Day", "Multiple days"])
    shift_scope = st.selectbox("What shift/hours are requested? *", [
        "Full day", "Beginning of shift", "End of shift", "Beginning and End of shift"
    ])
    start_time = st.text_input("Start Time * (HH:MM AM/PM)")
    lob_assist = st.multiselect("Which LoB is the advisor assisting with? *", [
        "Admin", "ERO", "IT", "MoveBuddy", "PS BO", "PS CC", "PS CM", "PS Sales", "PS WL",
        "QA", "SS CM", "SS Sales", "SS WL", "TL/LoD"
    ])
    skills_to_add = st.multiselect("Skill(s) to Add (max 2)", [
        "MoveBuddy", "PS CC EN", "PS CC FR", "PS Sales EN", "PS Sales FR", "PS Test",
        "PS WL EN", "PS WL FR", "SS CM EN", "SS CM FR", "SS Sales EN", "SS Sales FR",
        "SS Test", "SS WL EN", "SS WL FR"
    ], max_selections=2)
    hours_per_week = st.number_input("How many hours will they be working per week? *", min_value=1)
    notes = st.text_area("Additional Notes (e.g. CP3 approval, IT ticket number)")

    submitted = st.form_submit_button("Submit Additional Hours Request")

if submitted:
    st.success("✅ Additional hours request submitted.")
    # Add logic to save or pass data back to main ticket
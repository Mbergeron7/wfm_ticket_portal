import streamlit as st

st.title("🧠 CP Skill Update")

with st.form("cp_skill_form"):
    skills_to_add = st.multiselect("Skill(s) to Add (max 2)", [
        "MoveBuddy", "PS CC EN", "PS CC FR", "PS Sales EN", "PS Sales FR", "PS Test",
        "PS WL EN", "PS WL FR", "SS CM EN", "SS CM FR", "SS Sales EN", "SS Sales FR",
        "SS Test", "SS WL EN", "SS WL FR"
    ], max_selections=2)

    skills_to_remove = st.multiselect("Skill(s) to Remove (max 2)", [
        "MoveBuddy", "PS CC EN", "PS CC FR", "PS Sales EN", "PS Sales FR", "PS Test",
        "PS WL EN", "PS WL FR", "SS CM EN", "SS CM FR", "SS Sales EN", "SS Sales FR",
        "SS Test", "SS WL EN", "SS WL FR"
    ], max_selections=2)

    cp_name_change = st.text_area("If a CP name change is also needed, please note it here.")
    cp3_upload = st.file_uploader("📎 Upload CP3 Approval", type=["pdf", "jpg", "png"])
    notes = st.text_area("Additional Notes")

    submitted = st.form_submit_button("Submit CP Skill Update")

if submitted:
    st.success("✅ CP skill update submitted.")
    # Add logic to save or pass data back to main ticket
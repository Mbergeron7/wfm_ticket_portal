import streamlit as st

st.title("🕒 Is Overtime Available?")

with st.form("ot_availability_form"):
    lob_assist = st.multiselect("Which LoB is the advisor looking to assist with for OT/additional hours? *", [
        "Admin", "ERO", "IT", "MoveBuddy", "PS BO", "PS CC", "PS CM", "PS Sales", "PS WL",
        "QA", "SS CM", "SS Sales", "SS WL", "TL/LoD"
    ])
    
    st.markdown("📌 If a skill update is required, please submit a separate form:")
    st.markdown("[🔗 Skill Update Form](https://forms.office.com/r/jzKwy84EMS)")
    
    notes = st.text_area("Additional Notes (e.g. context, CP3 approval, IT ticket)")

    submitted = st.form_submit_button("Submit OT Inquiry")

if submitted:
    st.success("✅ OT availability inquiry submitted.")
    # Add logic to save or pass data back to main ticket
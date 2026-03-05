import streamlit as st

st.title("Check Voting Eligibility")

age = st.number_input("Enter age", step=1)
if st.button("Check"):
    if age >= 18:
        st.success("Eligible to vote")
    else:
        st.error("Not eligible to vote")
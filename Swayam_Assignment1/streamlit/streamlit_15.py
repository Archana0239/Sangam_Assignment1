import streamlit as st

st.title("Voting Eligibility Checker")

age = st.number_input("Enter your age", min_value=0, step=1, format="%d")

if st.button("Check"):
    if age >= 18:
        st.write("Eligible to vote")
    else:
        st.write("Not eligible to vote")
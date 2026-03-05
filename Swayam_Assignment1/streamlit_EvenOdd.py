import streamlit as st

st.title("Check Even or Odd")

n = st.number_input("Enter number", step=1)
if st.button("Check"):
    if n % 2 == 0:
        st.success("Even")
    else:
        st.error("Odd")
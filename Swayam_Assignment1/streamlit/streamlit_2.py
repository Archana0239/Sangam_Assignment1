import streamlit as st

st.title("Even or Odd Checker")

n = st.number_input("Enter a number", step=1, format="%d")

if st.button("Check"):
    if n % 2 == 0:
        st.write("Even")
    else:
        st.write("Odd")
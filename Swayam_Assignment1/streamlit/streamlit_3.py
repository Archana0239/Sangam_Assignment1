import streamlit as st

st.title("Factorial Calculator")

n = st.number_input("Enter a number", min_value=0, step=1, format="%d")

if st.button("Calculate"):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    st.write("Factorial:", fact)
import streamlit as st

st.title("Multiplication Table")

n = st.number_input("Enter a number", step=1, format="%d")

if st.button("Show Table"):
    for i in range(1, 11):
        st.write(f"{n} x {i} = {n * i}")
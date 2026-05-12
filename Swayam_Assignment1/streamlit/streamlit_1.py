import streamlit as st

st.title("Simple Calculator")

a = st.number_input("Enter first number", format="%.2f")
b = st.number_input("Enter second number", format="%.2f")

if st.button("Calculate"):
    st.write("Addition:", a + b)
    st.write("Subtraction:", a - b)
    st.write("Multiplication:", a * b)

    if b != 0:
        st.write("Division:", a / b)
    else:
        st.write("Division: Undefined")
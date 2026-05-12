import streamlit as st

st.title("Compare Two Numbers")

a = st.number_input("Enter first number", step=1, format="%d")
b = st.number_input("Enter second number", step=1, format="%d")

if st.button("Compare"):
    if a > b:
        st.write("First number is greater")
    elif b > a:
        st.write("Second number is greater")
    else:
        st.write("Both are equal")
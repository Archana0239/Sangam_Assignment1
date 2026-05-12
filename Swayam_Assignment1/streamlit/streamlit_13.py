import streamlit as st

st.title("Sum of Digits")

n = st.number_input("Enter a number", min_value=0, step=1, format="%d")

if st.button("Calculate"):
    s = 0
    temp = n

    while temp > 0:
        s += temp % 10
        temp //= 10

    st.write("Sum of digits:", s)
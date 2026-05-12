import streamlit as st

st.title("Print Numbers from 1 to N")

n = st.number_input("Enter a number", min_value=1, step=1, format="%d")

if st.button("Print"):
    for i in range(1, n + 1):
        st.write(i)
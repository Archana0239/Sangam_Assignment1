import streamlit as st

st.title("Positive, Negative or Zero")

n = st.number_input("Enter a number", step=1, format="%d")

if st.button("Check"):
    if n > 0:
        st.write("Positive")
    elif n < 0:
        st.write("Negative")
    else:
        st.write("Zero")
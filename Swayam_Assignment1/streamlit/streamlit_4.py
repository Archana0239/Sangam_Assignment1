import streamlit as st

st.title("Factors of a Number")

n = st.number_input("Enter a number", min_value=1, step=1, format="%d")

if st.button("Find Factors"):
    st.write("Factors are:")

    for i in range(1, n + 1):
        if n % i == 0:
            st.write(i)
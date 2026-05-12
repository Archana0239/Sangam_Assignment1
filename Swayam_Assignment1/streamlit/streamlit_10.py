import streamlit as st

st.title("Prime Number Checker")

n = st.number_input("Enter a number", min_value=1, step=1, format="%d")

if st.button("Check"):
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                st.write("Not Prime")
                break
        else:
            st.write("Prime")
    else:
        st.write("Not Prime")
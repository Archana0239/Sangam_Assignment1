import streamlit as st

st.title("Sum of List Elements")

nums = st.text_input("Enter numbers separated by space")

if st.button("Calculate Sum"):
    numbers = list(map(int, nums.split()))
    st.write("Sum:", sum(numbers))
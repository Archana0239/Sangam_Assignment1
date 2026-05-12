import streamlit as st

st.title("Student Grade Calculator")

name = st.text_input("Enter student name")

s1 = st.number_input("Enter marks for Subject 1", min_value=0, max_value=100, step=1)
s2 = st.number_input("Enter marks for Subject 2", min_value=0, max_value=100, step=1)
s3 = st.number_input("Enter marks for Subject 3", min_value=0, max_value=100, step=1)

if st.button("Calculate"):
    total = s1 + s2 + s3
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    st.write("Name:", name)
    st.write("Total:", total)
    st.write("Grade:", grade)
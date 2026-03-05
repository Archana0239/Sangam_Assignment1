import streamlit as st
import pandas as pd

st.set_page_config(page_title="Python Lab Experiments", layout="wide")

st.title("Python Lab Experiments Dashboard")
st.write("Select an experiment from the sidebar to view its execution.")

# --- Sidebar Navigation ---
experiments = [
    "1. Check Even or Odd",
    "2. Check Voting Eligibility",
    "3. Greatest of Two Numbers",
    "4. Sign of a Number",
    "5. Arithmetic Operations",
    "6. First 10 Natural Numbers",
    "7. First n Natural Numbers",
    "8. Multiplication Table (Given Number)",
    "9. Multiplication Table of 9",
    "10. Sum of Digits",
    "11. Factorial of a Number",
    "12. Factors of a Number",
    "13. Prime Number Check",
    "14. Sum of Elements in a List",
    "15. Student Grade Calculation"
]

selection = st.sidebar.selectbox("Choose an Experiment:", experiments)

st.divider()

# --- Experiment Implementations ---

if selection == "1. Check Even or Odd":
    st.header(selection)
    num = st.number_input("Enter an integer:", step=1, value=0)
    if num % 2 == 0:
        st.success(f"{num} is even.")
    else:
        st.info(f"{num} is odd.")

elif selection == "2. Check Voting Eligibility":
    st.header(selection)
    age = st.number_input("Enter your age:", min_value=0, step=1, value=18)
    if age >= 18:
        st.success("You are eligible to vote.")
    else:
        st.error("You are not eligible to vote.")

elif selection == "3. Greatest of Two Numbers":
    st.header(selection)
    col1, col2 = st.columns(2)
    num1 = col1.number_input("Enter the first number:", value=0.0)
    num2 = col2.number_input("Enter the second number:", value=0.0)

    if num1 > num2:
        st.success("The first number is greater.")
    elif num2 > num1:
        st.success("The second number is greater.")
    else:
        st.info("Both numbers are equal.")

elif selection == "4. Sign of a Number":
    st.header(selection)
    num = st.number_input("Enter a number:", value=0.0)
    if num > 0:
        st.success("Positive")
    elif num < 0:
        st.error("Negative")
    else:
        st.info("Zero")

elif selection == "5. Arithmetic Operations":
    st.header(selection)
    col1, col2 = st.columns(2)
    num1 = col1.number_input("First number:", value=0.0)
    num2 = col2.number_input("Second number:", value=0.0)

    st.write(f"**Addition:** {num1 + num2}")
    st.write(f"**Subtraction:** {num1 - num2}")
    st.write(f"**Multiplication:** {num1 * num2}")
    if num2 != 0:
        st.write(f"**Division:** {num1 / num2}")
    else:
        st.error("Division: Cannot divide by zero.")

elif selection == "6. First 10 Natural Numbers":
    st.header(selection)
    st.write("Using a `for` loop:")
    result = ""
    for i in range(1, 11):
        result += f"{i} "
    st.code(result)

elif selection == "7. First n Natural Numbers":
    st.header(selection)
    n = st.number_input("Enter a number n:", min_value=1, step=1, value=5)
    st.write("Using a `while` loop:")
    i = 1
    result = []
    while i <= n:
        result.append(str(i))
        i += 1
    st.code(" ".join(result))

elif selection == "8. Multiplication Table (Given Number)":
    st.header(selection)
    num = st.number_input("Enter a number for its multiplication table:", step=1, value=5)
    for i in range(1, 11):
        st.write(f"{num} x {i} = {num * i}")

elif selection == "9. Multiplication Table of 9":
    st.header(selection)
    for i in range(1, 11):
        st.write(f"9 x {i} = {9 * i}")

elif selection == "10. Sum of Digits":
    st.header(selection)
    num = st.number_input("Enter a number:", step=1, value=123)
    temp = abs(num)
    total_sum = 0
    while temp > 0:
        digit = temp % 10
        total_sum += digit
        temp //= 10
    st.success(f"The sum of the digits is: {total_sum}")

elif selection == "11. Factorial of a Number":
    st.header(selection)
    num = st.number_input("Enter a number:", min_value=0, step=1, value=5)
    factorial = 1
    if num == 0:
        st.success("The factorial of 0 is 1.")
    else:
        for i in range(1, num + 1):
            factorial *= i
        st.success(f"The factorial of {num} is {factorial}.")

elif selection == "12. Factors of a Number":
    st.header(selection)
    num = st.number_input("Enter a number:", min_value=1, step=1, value=12)
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(str(i))
    st.write(f"The factors of {num} are:")
    st.code(", ".join(factors))

elif selection == "13. Prime Number Check":
    st.header(selection)
    num = st.number_input("Enter a number:", min_value=1, step=1, value=7)
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            st.success(f"{num} is a prime number.")
        else:
            st.error(f"{num} is not a prime number.")
    else:
        st.error(f"{num} is not a prime number.")

elif selection == "14. Sum of Elements in a List":
    st.header(selection)
    user_input = st.text_input("Enter numbers separated by commas:", "10, 25, 30, 45")
    try:
        # Convert string input into a list of floats
        numbers = [float(x.strip()) for x in user_input.split(",")]
        st.write(f"**Current List:** {numbers}")
        st.success(f"**Sum of elements:** {sum(numbers)}")
    except ValueError:
        st.error("Please enter valid numbers separated by commas.")

elif selection == "15. Student Grade Calculation":
    st.header(selection)
    name = st.text_input("Enter student's name:", "John Doe")
    col1, col2, col3 = st.columns(3)
    maths = col1.number_input("Maths Marks:", min_value=0.0, max_value=100.0, value=85.0)
    physics = col2.number_input("Physics Marks:", min_value=0.0, max_value=100.0, value=90.0)
    chemistry = col3.number_input("Chemistry Marks:", min_value=0.0, max_value=100.0, value=88.0)

    total_marks = maths + physics + chemistry
    percentage = (total_marks / 300) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "Fail"

    st.write("### Result")
    st.write(f"**Name:** {name}")
    st.write(f"**Total Marks:** {total_marks} / 300")
    st.write(f"**Percentage:** {percentage:.2f}%")
    st.write(f"**Grade:** {grade}")
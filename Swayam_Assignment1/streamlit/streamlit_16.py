import streamlit as st
import pandas as pd

st.title("CSV File Reader")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write(df)

    except FileNotFoundError:
        st.write("CSV file not found")

    except Exception as e:
        st.write("Error:", e)
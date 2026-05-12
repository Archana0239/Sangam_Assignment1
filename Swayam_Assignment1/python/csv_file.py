import pandas as pd

try:
    df = pd.read_csv("data.csv")
    print(df)

except FileNotFoundError:
    print("CSV file not found")

except Exception as e:
    print("Error:", e)
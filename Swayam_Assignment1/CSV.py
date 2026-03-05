import pandas as pd

file = input()
df = pd.read_csv(file)
print(df.head(10))
import pandas as pd

df = pd.read_csv("students.csv")

print(df)
print("Sum =", df["marks"].sum())
print("Mean =", df["marks"].mean())
print("Max =", df["marks"].max())
print("Min =", df["marks"].min())

import pandas as pd


df = pd.read_csv("wa_names.csv")

df.drop_duplicates()
print(df)
df.to_csv("wa_names.csv", index=False)
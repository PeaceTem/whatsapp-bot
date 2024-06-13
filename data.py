import pandas as pd


data = pd.read_json("wa2_contacts.json")

data.to_csv("wa2_contacts.csv", index=False)
df = pd.read_csv("wa2_contacts.csv")
data = df["name"]
data = data.dropna()
print(data)

data.to_csv("wa_names.csv", index=False)

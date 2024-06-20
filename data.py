import pandas as pd


data = pd.read_json("new_wa_contacts.json")

data.to_csv("new_wa_contacts.csv", index=False)
df = pd.read_csv("new_wa_contacts.csv")
data = df["name"]
data = data.dropna()
data.to_csv("new_contacts.csv", index=False)

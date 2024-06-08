import pandas as pd


# data = pd.read_json("record.json")

# data.to_csv("my_contacts.csv", index=False)
df = pd.read_csv("my_contacts.csv")
data = df["name"]
data = data.dropna()
print(data)

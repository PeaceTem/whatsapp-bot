import pandas as pd
import numpy as np






df = pd.read_csv("new_contacts.csv")

df.drop_duplicates()
# Split the DataFrame into 4 parts
dfs = np.array_split(df, 2000)

print(dfs[0]["Name"].tolist())


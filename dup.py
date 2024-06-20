import pandas as pd
import numpy as np

df = pd.read_csv("new_contacts.csv")

df.drop_duplicates()
dfs = np.array_split(df, 4)
print(dfs[0])
print(dfs[1])
print(dfs[2])

print(dfs[3])

import pandas as pd


data = pd.read_csv("apapa.csv")

data.head()

print(data["Name"].tolist())

# df['new_column'] = my_list
# # Save the modified DataFrame back to a CSV file
# df.to_csv('modified_file.csv', index=False)

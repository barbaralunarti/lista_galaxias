# %%

import pandas as pd

# %%

df = pd.read_csv("faundez_mariangela.txt", sep="\t", header=None)
df

# %%

df.rename(columns={0: 'A', 1: 'Object', 2: 'RA', 3: 'DEC', 4: 'E', 5: 'F'}, inplace=True)
df

# %%

df.drop(columns=['A', 'E', 'F'], inplace=True)

# %%

df["Class"] = "PRG"
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df

# %%

df.to_csv('faundez_mariangela.csv', index=False)

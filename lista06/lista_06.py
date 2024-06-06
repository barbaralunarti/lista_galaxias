# %%

import pandas as pd

# %%

df = pd.read_csv('faundez_ramirez_hertling.txt', sep='  ')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df

# %%

df.to_csv('lista_faundez_ramirez_hertling.csv')

# %%

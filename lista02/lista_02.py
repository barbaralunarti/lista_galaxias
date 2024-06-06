# %%
import pandas as pd

# %%
df = pd.read_csv('moiseevetal_whitmoreetal.txt', sep='  ')
df
# %%

novo_df = df.drop('z', axis=1)
novo_df.to_csv('lista_moiseevetal_whitmoreetal.csv')

# %% 
import pandas as pd

# %% 

df = pd.read_csv('theys_and_spiegel.txt', sep='  ')
df

# %%
df.to_csv('lista_theys_and_spiegel.csv')
# %%

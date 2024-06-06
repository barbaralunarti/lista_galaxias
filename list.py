# %%

import pandas as pd
import os
import csv

# %%

path_file01 = 'lista01/lista_arp_madore.csv'
df_01 = pd.read_csv(path_file01)
df_01

# %%

path_file02 = 'lista02/lista_moiseevetal_whitmoreetal.csv'
df_02 = pd.read_csv(path_file02)
df_02

# %%

path_file03 = 'lista03/lista_madore_nelson.csv'
df_03 = pd.read_csv(path_file03)
df_03

# %%

path_file04 = 'lista04/lista_theys_and_spiegel.csv'
df_04 = pd.read_csv(path_file04)
df_04

# %%

path_file05 = 'lista05/lista_faundez_cuevas_hertling.csv'
df_05 = pd.read_csv(path_file05)
df_05

# %%

path_file06 = 'lista06/lista_faundez_ramirez_hertling.csv'
df_06 = pd.read_csv(path_file06)
df_06

# %%

path_file07 = 'lista07/lista_faundez_mariangela.csv'
df_07 = pd.read_csv(path_file07)
df_07

# %%

columns_to_select = ["Object", "RA", "DEC", "Class"]
df_01 = df_01[columns_to_select]
df_02 = df_02[columns_to_select]
df_03 = df_03[columns_to_select]
df_04 = df_04[columns_to_select]
df_05 = df_05[columns_to_select]
df_06 = df_06[columns_to_select]
df_07 = df_07[columns_to_select]

combined_df = pd.concat([df_01, df_02, df_03, df_04, df_05, df_06, df_07], ignore_index=True)

# %%

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
combined_df

# %%

combined_df.to_csv('list_ring_galaxies.csv', index=False)

# %%

df_prg = pd.read_csv('list_ring_galaxies.csv')
df_prg

# %%

df_prg = df_prg[df_prg['Class'] == 'PRG']
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df_prg

# %%

drop_duplicates = df_prg.drop_duplicates(subset=['Object'], keep='first')
drop_duplicates

# %%

drop_duplicates.to_csv('prg.csv', index=False)

# %%

prg = pd.read_csv('prg.csv')
prg

# %%

df_sorted = prg.sort_values(by='Object')
df_sorted

# %%

df_sorted = df_sorted.reset_index(drop=True)
df_sorted

# %%

df_sorted.to_csv('prg.csv')
# %%

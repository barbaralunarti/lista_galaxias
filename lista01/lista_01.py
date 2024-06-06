# %%

import pandas as pd

# %%

column_widths = [12, 10]
column_names = ['col1', 'col2']
df = pd.read_fwf('arp_and_madore_86.txt', widths=column_widths, names=column_names)
print(df)

# %%

df['col3'] = pd.Series([None] * len(df))
for index, row in df.iterrows():
    if pd.isnull(row['col1']) or str(row['col1']).startswith('[') or str(row['col1'] == '?'):
        df.at[index - 1, 'col3'] = row['col2']

df = df[~(df['col1'].isnull() | df['col1'].astype(str).str.startswith('[') | (df['col1'] == '?'))]

# %%

novos_nomes = {'col1':'Object', 'col2': 'RA', 'col3': 'DEC'}
df = df.rename(columns=novos_nomes)
df = df.sort_index()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df['Class'] = 'PRG'
df.to_csv('am86.csv', index=False)
df

# %%

# Atualização manual das coordenadas RA e DEC em arp_madore.csv a partir dos dados em am86.csv.

# %%

df = pd.read_csv('arp_madore.csv', index_col=False)
df.drop(columns=['Unnamed: 0'], inplace=True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df

# %%

# Removendo 3 objetos (que são galáxias espirais na literatura) e uma nebulosa planetária:

df.drop([137, 143, 151, 267], inplace=True)

# %%

df.reset_index(inplace=True, drop=True)
df

# %%

df.to_csv('lista_arp_madore.csv', index=False)
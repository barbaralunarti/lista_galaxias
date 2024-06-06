# %%

import pandas as pd

# %%

with open('madore_and_nelson_2009.txt', 'r') as file:
    content = file.read()

lines = content.strip().split('\n')

rows = []
current_header = None

for line in lines:
    parts = line.split('\t')
    print(len(parts))
    if len(parts) == 6:
        obj_name = parts[0]
        other_values = parts[1:]
        row_data = [obj_name] + other_values
        rows.append(row_data)

columns = ["Object"] + [f"Column{i}" for i in range(len(other_values))]
df = pd.DataFrame(rows, columns=columns)
df

# %%

novos_nomes = {'Column0':'RA', 'Column1':'DEC'}
df = df.rename(columns=novos_nomes)

# %%

df = df.drop('Column2', axis=1)
df

# %%

df = df.drop('Column3', axis=1)
df

# %%

df = df.drop('Column4', axis=1)
df

# %%

df = df.drop(27, axis=0)
df

# %%

df['Object'] = df['Object'].str.replace(':RN', '')
df

# %%

df['RA'] = df['RA'].str.replace(':', ' ')
df

# %%

df['DEC'] = df['DEC'].str.replace(':', ' ')
df

# %%

df.to_csv('lista_madore_nelson.csv')
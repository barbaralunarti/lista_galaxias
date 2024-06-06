# %%

import pandas as pd

# %%

data_types = {'Column1': int, 'Object': str, 'Column3': str, 'Column4': str, 'Column5': str, 
              'Column6': str, 'Column7': str, 'RA': str, 'DEC': str, 'Column10': str}

df = pd.read_csv('faundez_cuevas_hertling.csv', index_col=0, dtype=data_types)
df

# %%

colunas_para_remover = ['Column1', 'Column3', 'Column4', 'Column5', 'Column7', 'Column10']
df = df.drop(columns=colunas_para_remover)
df

# %%

def update_column6(value):
    if isinstance(value, str) and (value.startswith('SB') or value.startswith('Sa')):
        return 'NRG'
    else:
        return value

df['Column6'] = df['Column6'].apply(update_column6)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df

# %%

def update_column6(value):
    if isinstance(value, str) and (value.startswith('El') or value.startswith('Sp')):
        return 'PRG'
    else:
        return value

df['Column6'] = df['Column6'].apply(update_column6)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df

# %%

def corrigir_dataframe(df, indice_correcao, novo_valor_column6, novo_valor_ra, novo_valor_dec):
    df.at[indice_correcao, 'Column6'] = novo_valor_column6
    df.at[indice_correcao, 'RA'] = novo_valor_ra
    df.at[indice_correcao, 'DEC'] = novo_valor_dec
    return df

indice_correcao = 46
novo_valor_column6 = 'PRG'
novo_valor_ra = '05 47 06.2'
novo_valor_dec = '-80 18 36'
df_corrigido = corrigir_dataframe(df.copy(), indice_correcao, novo_valor_column6, novo_valor_ra, novo_valor_dec)
df_corrigido

# %%

df = df_corrigido
df

# %%

df['Column6'].fillna('NRG', inplace=True)
df

# %%

df = df[['Object', 'RA', 'DEC', 'Column6']].rename(columns={'Column6': 'Class'})

# %%

df['Object'] = 'HRG ' + df['Object']

# %%

df.to_csv('lista_faundez_cuevas_hertling.csv', index=False)
# %%

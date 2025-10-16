import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
df = pd.read_csv("C:\git\Git_haspian\Trabalhos\Implanew\IMPLANEW.csv", sep=';')
df = df[df['CODIGO'].notnull()]

#print(df)

for i in range(1, 18):
    df.loc[df[f'DIM_{i}'] == '-', f'DIM_{i}'] = 0
    df.loc[df[f'SUP_{i}'] == '-', f'SUP_{i}'] = 0
    df.loc[df[f'INF_{i}'] == '-', f'INF_{i}'] = 0
    df[f'DIM_{i}'] = pd.to_numeric(df[f'DIM_{i}'], errors='coerce').replace(np.nan, 0)
    df[f'SUP_{i}'] = pd.to_numeric(df[f'SUP_{i}'], errors='coerce').replace(np.nan, 0)
    df[f'INF_{i}'] = pd.to_numeric(df[f'INF_{i}'], errors='coerce').replace(np.nan, 0)

print(df)

df['DIM_1'] = df['DIM_1'].astype('float')
df['SUP_1'] = df['SUP_1'].astype('float')
df['INF_1'] = df['INF_1'].astype('float')
df['DIM_2'] = df['DIM_2'].astype('float')
df['SUP_2'] = df['SUP_2'].astype('float')
df['INF_2'] = df['INF_2'].astype('float')
df['DIM_3'] = df['DIM_3'].astype('float')
df['SUP_3'] = df['SUP_3'].astype('float')
df['INF_3'] = df['INF_3'].astype('float')
df['DIM_4'] = df['DIM_4'].astype('float')
df['SUP_4'] = df['SUP_4'].astype('float')
df['INF_4'] = df['INF_4'].astype('float')
df['DIM_5'] = df['DIM_5'].astype('float')
df['SUP_5'] = df['SUP_5'].astype('float')
df['INF_5'] = df['INF_5'].astype('float')
df['DIM_6'] = df['DIM_6'].astype('float')
df['SUP_6'] = df['SUP_6'].astype('float')
df['INF_6'] = df['INF_6'].astype('float')
df['DIM_7'] = df['DIM_7'].astype('float')
df['SUP_7'] = df['SUP_7'].astype('float')
df['INF_7'] = df['INF_7'].astype('float')
df['DIM_8'] = df['DIM_8'].astype('float')
df['SUP_8'] = df['SUP_8'].astype('float')
df['INF_8'] = df['INF_8'].astype('float')
df['DIM_9'] = df['DIM_9'].astype('float')
df['SUP_9'] = df['SUP_9'].astype('float')
df['INF_9'] = df['INF_9'].astype('float')
df['DIM_10'] = df['DIM_10'].astype('float')
df['SUP_10'] = df['SUP_10'].astype('float')
df['INF_10'] = df['INF_10'].astype('float')
df['DIM_11'] = df['DIM_11'].astype('float')
df['SUP_11'] = df['SUP_11'].astype('float')
df['INF_11'] = df['INF_11'].astype('float')
df['DIM_12'] = df['DIM_12'].astype('float')
df['SUP_12'] = df['SUP_12'].astype('float')
df['INF_12'] = df['INF_12'].astype('float')
df['DIM_13'] = df['DIM_13'].astype('float')
df['SUP_13'] = df['SUP_13'].astype('float')
df['INF_13'] = df['INF_13'].astype('float')
df['DIM_14'] = df['DIM_14'].astype('float')
df['SUP_14'] = df['SUP_14'].astype('float')
df['INF_14'] = df['INF_14'].astype('float')
df['DIM_15'] = df['DIM_15'].astype('float')
df['SUP_15'] = df['SUP_15'].astype('float')
df['INF_15'] = df['INF_15'].astype('float')
df['DIM_16'] = df['DIM_16'].astype('float')
df['SUP_16'] = df['SUP_16'].astype('float')
df['INF_16'] = df['INF_16'].astype('float')
df['DIM_17'] = df['DIM_17'].astype('float')
df['SUP_17'] = df['SUP_17'].astype('float')
df['INF_17'] = df['INF_17'].astype('float')

df = df[df['CODIGO'].notnull()]
pd.set_option('float_format', '{:.3f}'.format)
print(df.dtypes)

PartCode = []
Description = []
NominalValue = []
MinValue = []
MaxValue = []

for ind, linha in df.iterrows():
    for i in range(1, 18):
        if linha[f'ITEM_{i}'] == '-':
            break
        else:
            PartCode.append(linha['CODIGO'])
            Description.append(f'{linha[f'ITEM_{i}']} {linha[f'CRITERIO_{i}']}')
            NominalValue.append(f'{linha[f'DIM_{i}']}')
            m_sup = float(linha[f'DIM_{i}']) + float(linha[f'SUP_{i}'])
            MaxValue.append(m_sup)
            m_inf = float(linha[f'DIM_{i}']) + float(linha[f'INF_{i}'])
            MinValue.append(m_inf)

df_implanew = pd.DataFrame(data={'PartCode': PartCode,
                                 'Description': Description,
                                 'NominalValue': NominalValue,
                                 'MaxValue': MaxValue,
                                 'MinValue': MinValue
                                 }
                           )

print(df_implanew)
df_implanew.to_excel('C:\\git\\Git_haspian\\Trabalhos\\Implanew\\teste.xlsx', index=False)

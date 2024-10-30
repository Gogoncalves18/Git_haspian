import pandas as pd

lt = [['N00003', '1002', 435360.0], ['N00004', '1003', 435360.0], ['N00005', '1003', 4360.0]]
    
df = pd.DataFrame(lt, columns=['ARRANJOS', 'OF', 'CODPECA'])

# print(df)
li = set()

nu = 1002


# for i, raw in df.iterrows():
#     li.add(str(raw['OF']))


for i, raw in df.iterrows():
    if nu == int(raw['OF']):
        # print(f'Achei o {nu}')
        pass

df_imp = df[df['OF'] == '1003']

print(df_imp)






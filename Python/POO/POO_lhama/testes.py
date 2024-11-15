import pandas as pd

dados = {1: [1, 2, 11, 121], 2: [1, 2, 22, 32], 3: [11, 121, 22, 32]}

df = pd.DataFrame.from_dict(data=dados, orient='index')

print(df)
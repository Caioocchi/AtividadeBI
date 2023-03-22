import pandas as pd

df = pd.read_csv('MICRODADOS.csv', delimiter=';', encoding='latin-1')
df['DataObito'] = pd.to_datetime(df['DataObito'])
inicio = pd.to_datetime('2020-01-01')
fim = pd.to_datetime('2023-12-31')
df_filtrado = df[(df['Municipio'] == 'CARIACICA') & (df['ComorbidadeTabagismo'] == 'Sim') & (df['DataObito'] >= inicio) & (df['DataObito'] <= fim)]
df_filtrado.to_csv('MICRODADOS_filtrado.csv', index=False)
print(df_filtrado)
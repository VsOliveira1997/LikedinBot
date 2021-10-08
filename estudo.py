import pandas as pd

data = {
    'nome': 'jooao',
    'cargo': 'Admin'
}

df = pd.DataFrame([data], columns=['nome','cargo'], index=)
df.to_csv('dados_final.csv', mode='a')
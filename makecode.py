import pandas as pd

data = pd.read_csv('from.csv', dtype=str)

with open('from.json','w',encoding='utf-8') as file:
    data.to_json(file, force_ascii=False, orient='table')
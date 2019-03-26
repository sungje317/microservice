import pandas as pd

data = pd.read_csv('stock_code.csv', dtype=str)

with open('stock_code.json','w',encoding='utf-8') as file:
    data.to_json(file, force_ascii=False, orient='table')

data = pd.read_csv('class.csv', dtype=str)

with open('class.json','w',encoding='utf-8') as file:
    data.to_json(file, force_ascii=False, orient='table')

data = pd.read_csv('from.csv', dtype=str)

with open('from.json','w',encoding='utf-8') as file:
    data.to_json(file, force_ascii=False, orient='table')

data = pd.read_csv('reason.csv', dtype=str)

with open('reason.json','w',encoding='utf-8') as file:
    data.to_json(file, force_ascii=False, orient='table')
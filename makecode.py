import pandas as pd

data = pd.read_csv('class.csv', dtype=str)

with open('class.json','w',encoding='utf-8') as file:
    data.to_json(file, force_ascii=False, orient='table')
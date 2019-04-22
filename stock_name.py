import pandas as pd

code_df_kosdaq = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=kosdaqMkt', header=0)[0]
code_df_kosdaq.종목코드 = code_df_kosdaq.종목코드.map('{:06d}'.format)
code_df_kosdaq = code_df_kosdaq[['회사명', '종목코드']]
code_df_kosdaq = code_df_kosdaq.rename(columns={'회사명': 'name', '종목코드': 'code'})
print(code_df_kosdaq.head())

code_df_kospi = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=stockMkt', header=0)[0]
code_df_kospi.종목코드 = code_df_kospi.종목코드.map('{:06d}'.format)
code_df_kospi = code_df_kospi[['회사명', '종목코드']]
code_df_kospi = code_df_kospi.rename(columns={'회사명': 'name', '종목코드': 'code'})
print(code_df_kospi.head())

code_df = code_df_kosdaq
code_df = code_df.append(code_df_kospi)

with open('stock_name.json','w',encoding='utf-8') as file:
    code_df.to_json(file, force_ascii=False, orient='table')
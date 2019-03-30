import datetime
import bs4 as BeautifulSoup
import requests
import pandas as pd
import json

def get_url(code):
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
    return url

def get_backdata(url):

    df = pd.DataFrame(columns=['date', 'close', 'diff', 'open', 'high', 'low', 'volume'])
    try:
        pg_url = '{url}&page={page}'.format(url=url, page=1)
        df = pd.read_html(pg_url, header=0)[0]
        df = df.dropna()
        df = df.rename(columns={'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})
        df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by=['date'], ascending=False)
    except :
        return None, True

    df = df.reset_index(drop=True)

    df['date'] = pd.to_datetime(df['date'], format="%m/%d")
    df['open'] = pd.to_numeric(df['open'])
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])
    df['close'] = pd.to_numeric(df['close'])

    return df, False

def get_class(Class, Subclass):
    RealURL = APIURL + 'Class=' + Class + '&Subclass=' + Subclass
    result = requests.get(RealURL, headers=HEADER)
    result = result.text
    result = json.loads(result)
    result = result[0]
    return result["Cname"], result["Sname"]

TEMP = "/home/ubuntu/microservice/"
TEMP = "/Users/parksang-yeon/microservice/"
AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
APIURL = 'http://133.186.146.218:8000/class/data?'
HEADER = {'user-agent':AGENT, 'apikey':'vSBA8hHLWw6Nm8ynJC4CbsOkcdIGjHia'}

stock_code = pd.read_csv(TEMP+"stock_code.csv", dtype=str)
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(hours=7)



while datetime.datetime.now() < end_time :
    new_data = pd.DataFrame(columns=['code', 'name', 'className', 'subclassName', 'price', 'volume', 'percent'])
    for index in range(stock_code.shape[0]):
        code = stock_code.loc[index]["StockCode"]
        name = stock_code.loc[index]["StockName"]
        Class = stock_code.loc[index]["Class"]
        Subclass = stock_code.loc[index]["Subclass"]

        print(name)

        className, subclassName = get_class(Class, Subclass)

        url = get_url(code)
        df, empty = get_backdata(url)
        if empty:
            continue

        price = df["close"][0]
        volume = df["volume"][0]
        diff = df["diff"][0]
        percent = str(round(diff * 100 / price, 2))
        new_data.loc[index] = [code, name, className, subclassName, price, volume, percent]
    with open('now_stock.json', 'w', encoding='utf-8') as file:
        new_data.to_json(file, force_ascii=False, orient='table')

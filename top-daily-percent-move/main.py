import json

import pandas as pd
import requests
from requests.exceptions import HTTPError

URL = "https://query1.finance.yahoo.com/v7/finance/chart/{}?range={" \
      "}&interval=1d&indicators=quote&includeTimestamps=true "


def getAnalysis(tickers="MSFT,F,CMG", range="3mo"):
    ts = tickers.split(",")
    res = []
    for ticker in ts:
        url = URL.format(ticker, range)
        data = getData(url)
        timestamps = data['timestamp']
        prices = data['indicators']['quote'][0]['close']
        df = pd.DataFrame(zip(timestamps, prices), columns=['date', 'price'])
        df.date = pd.to_datetime(df.date, unit='s').dt.floor('D')
        df = df.set_index("date")

        daily = (df / df.shift(1) - 1) * 100

        daily = daily.sort_values(by="price", ascending=False, key=abs)
        area_dict = dict(zip(daily[:5].index, daily[:5].price))
        tmp = []
        for k, v in area_dict.items():
            tmp.append({'date': k.strftime('%Y-%m-%d'), 'move': round(v, 2)})
        res.append({ticker: tmp})
    res_json = json.dumps(res)
    # print(res_json)
    return res_json


def getData(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
        return resp.json()['chart']['result'][0]

if __name__ == '__main__':
    getAnalysis()

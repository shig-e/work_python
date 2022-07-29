#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import os
import requests
import pandas as pd
import re

from dotenv import load_dotenv

load_dotenv('.env')

RAKUTEN_API_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"



def main():
    # 課題1
    data = []
    max_page = 10
    for i in range(1, max_page+1):
        params = {
            "applicationId": os.environ.get('APP_ID'),
            "format": "json",
            "keyword": search_keywrod,
            "page": i,
            "hits": 30}
        res = requests.get(RAKUTEN_API_URL, params)
        sleep(3)
        items = res.json()
        for _item in items["Items"]:
            item = _item["Item"]
            name = item["itemName"].replace("\u3000", ",")
            price = int(item['itemPrice'])
            url = item['itemUrl']
            discription = item['itemCaption'].replace("\u3000", ",")
            m = re.search(r'[0-9]{13}', discription)
            if m is not None:
                jancode = m.group()
            else:
                jancode = None

            data.append({"商品名": name,
                        "価格": price,
                        "url": url,
                        "説明文": discription,
                        "Jancode": jancode})
            df = pd.DataFrame(data)
            # 課題 2
            df.to_csv("rakuten_search.csv", encoding="utf-8")
    '''
    [課題]
    (1)
    楽天APIを使用して、以下の情報を取得してみよう!
    - 商品の価格
    - 商品のURL
    - 商品の説明
    - JANコード(難易度高: URLや商品説明欄から13桁の数値があった場合、それを取得するよう実装してみてください！)

    (2)
    結果をCSVファイルとして出力してみよう

    [準備]
    1. 仮想環境を構築(terminalで以下のコマンドを実行する)
        python -m venv venv

    2. 仮想環境に入る(terminalで以下のコマンドを実行する)
        source venv/bin/activate

    3. 仮想環境の中でライブラリをインストール(terminalで以下のコマンドを実行する)
        pip install --upgrade pip
        pip install requests
    '''


if __name__ == "__main__":
    search_keywrod = input("検索した商品を入力してください >>>")
    main()
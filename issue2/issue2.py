#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main():
    '''
    (例) 「ねこ」とターミナルに出力してください。

    (1) 以下の`products`はある商品とその価格の辞書型で定義されています。walletの価格を
        ターミナルに出力してください。
        解答:
            50000

    (2) `products`に「商品名:tablet, 価格:60000」を追加してください。その後、`products`の
        中身を以下の解答欄の形式でターミナルに出力してください。
        解答:
            tv 30000
            smartphone 100000
            wallet 50000
            tablet 60000

    (3) 1~200000までのランダムな整数`num`が与えられます。`products`の商品の中から
        価格が`num`以下の商品の場合は「商品名: Yes」価格が`num`より大きい場合は「商品名: No」
        とターミナルに出力してください。
        解答:
            たとえば、num が 86135 のときは以下の出力します。

            tv: Yes
            smartphone: No
            wallet: Yes
            tablet: Yes
    '''

    # (例)
    print("ねこ")

    products = {
        "tv": 30000,
        "smartphone": 100000,
        "wallet": 50000,
    }

    # (1)
    print(products["wallet"])
    print("="*30)
    # (2)
    products["tablet"] = 60000
    for item, price in products.items():
        print(item, price)
    print("="*30)
    # (3)
    num = random.randint(1, 200000)
    print(num)
    for item, price in products.items():
        if price < num:
            price = "Yes"
        elif price > num:
            price = "No"
        print(item, price)


if __name__ == "__main__":
    main()

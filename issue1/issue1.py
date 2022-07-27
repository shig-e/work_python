#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    '''
    (例) 「ねこ」とターミナルに出力してください。

    (1) sample1.txtから文字を読み取り、ファイルに記載している文字列をターミナルに出力してください。
        解答:
        北海道,青森県,岩手県,宮城県...

    (2) (1)で読み取った文字列を','で分割し、str型からlist型に変換して、以下のように出力してください
        解答:
            0 北海道
            1 青森県
            2 岩手県
            ...
    (3) sample2.txtファイルも読み取り、(1)の結果を合わせて以下解答のように出力してください。
        解答:
        0 北海道 sapporo
        1 青森県 aomori
        2 岩手県 morioka
        ...
    (4) (3)の結果を`result.csv`というファイル名で、CSVファイルとして出力してください。
    '''
    import pandas as pd
    # (例)
    # print("ねこ")
    
    # # 課題2
    with open("sample1.txt", "r", encoding="utf-8") as sample1:
        sample1 = sample1.read()
        print(sample1)
    
    # # 課題3
    todoufukens = sample1.split(",")
    for i, todoufuken in enumerate(todoufukens):
        print(i, todoufuken)
        
    # 課題4
    with open("sample2.txt", "r", encoding="utf-8") as sample2:
        sample2 = sample2.read()
        outputs =sample2.split("\n")
        print(type(outputs))
        
    data = []
    for i, (todoufuken, output) in enumerate(zip(todoufukens, outputs)):
        data.append({
                    "都道府県(漢字)": todoufuken,
                    "都道府県(ローマ字)": output})
        df = pd.DataFrame(data)
        df.to_csv("result.csv", encoding="utf-8")
        
if __name__ == "__main__":
    main()

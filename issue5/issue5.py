#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import pandas as pd
from lib2to3.pgen2 import driver
import logging

from config import logging_config  # loggingの設定を読み込むためimportしている
from chrome_driver import ChromeDriver


from output import Output

logger = logging.getLogger(__name__)


def main():
    """
    [目標]
    Pythonのクラスについて理解を深めよう!

    [課題]
    LancersのHPから、仕事情報を取得して、CSVファイルとして出力してみよう!
    https://www.lancers.jp/work/search?open=1&ref=header_menu

    [スクレイピング&ファイル出力する情報]
    - 記事タイトル
    - 記事URL
    - 投稿者名
    - 投稿者URL

    [条件]
    1. chrome_driver.pyを利用してスクレイピングしてみよう!(足りないメソッドがあったら実装してみよう!)
    2. output.pyのOutputクラスにファイルの出力に関する処理を実装してみよう!
    """

    logger.info("Start")

    chrome_driver = ChromeDriver()
    output = Output()
    df = pd.DataFrame()
    
    chrome_driver.open_url(
        "https://www.lancers.jp/work/search?open=1&ref=header_menu")
    sleep(3)
    
    
    elements =[]
    chrome_driver.get_elements("div.c-media__content > div.c-media__content__right", elements)
    for elem in elements:
        try:
            _title = chrome_driver.get_text(elem, "div.c-media__content > div.c-media__content__right > a > span")
            title = _title.replace("\n", " ")
            item_url = chrome_driver.item_get_url(elem, "div.c-media__content > div.c-media__content__right > a")
            _name = chrome_driver.get_text(elem, "div.c-media__job-lancer-status__right.c-media__thumbnail.c-avatar.c-avatar--small")
            name = _name.replace("\n", " ")
            name_url = chrome_driver.item_get_url(elem, "div.c-media__job-lancer-status__right.c-media__thumbnail.c-avatar.c-avatar--small > a")
            df = df.append({
                "記事タイトル": title,
                "記事URL": item_url,
                "記事制作者": name,
                "制作者URL": name_url},
                ignore_index=True)
            
        except Exception as e:
            print(e)
    # output.write_csv("lancers_production", df)
    df.to_csv("a", encoding="utf-8")
        
            
   
    # 以下に続きを実装してみよう！

    chrome_driver.close_driver()


if __name__ == "__main__":
    main()


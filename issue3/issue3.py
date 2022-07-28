#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def create_chrome_driver():

    options = ChromeOptions()
    # UserAgent
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
    options.add_argument('--ignore-ssl-errors')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["acceptInsecureCerts"] = True
    options.add_argument("--window-size=1400,900")
    options.add_argument('--incognito')
    options.add_experimental_option("detach", True)

    return Chrome(executable_path=ChromeDriverManager().install(),
                  options=options,
                  desired_capabilities=capabilities)


def main():

    # driverを生成
    driver = create_chrome_driver()
    # 課題1
    url = " https://www.python.org/"
    driver.get(url)

    df = pd.DataFrame()
    div_elem = driver.find_element(by=By.CSS_SELECTOR, value="#container")
    _elem_li = div_elem.find_elements(by=By.CSS_SELECTOR, value="#container > li.tier-1 ")
    for elem_li in _elem_li:
        _li = elem_li.find_elements(by=By.TAG_NAME, value="a")
        for li in _li:
            title = li.text
            url = li.get_attribute("href")
            df = df.append({"title": title,
                            "url": url},
                        ignore_index=True)
    # 課題2
    df.to_csv("python_org.csv", encoding="utf-8")
    '''
    [課題]
    (1)
    以下のPythonURLから、issue3_caputure.pngの画像に載っているの文字列とそのURLを全て取得してみよう!
    https://www.python.org/
    
    (2) 
    取得結果はCSVファイルとしてファイル出力してみよう!

    [準備]
    1. 仮想環境を構築(terminalで以下のコマンドを実行する)
        python -m venv venv

    2. 仮想環境に入る(terminalで以下のコマンドを実行する)
        source venv/bin/activate

    3. 仮想環境の中でライブラリをインストール(terminalで以下のコマンドを実行する)
        pip install --upgrade pip
        pip install selenium webdriver-manager
    '''

    # 以下にプログラムを実装してみよう！

    # driverを削除する
    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()

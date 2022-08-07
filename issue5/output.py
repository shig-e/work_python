#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from pathlib import Path


import logging

CSV_FILE_PATH = "./csv/{file_name}_{datetime}_data.csv"
log = logging.getLogger


class Output(object):
    """
    ファイル出力に関する処理はこのクラスのメソッドとして実装してみよう！
    """
    def __init__(self, file_name):
        self.file_name = file_name       
        


    def write_csv(self, df) -> bool:
        # csvフォルダがなければ作成
        dir = Path("./csv")
        dir.mkdir(parents=True, exist_ok=True)
        # path作成
        csv_path = CSV_FILE_PATH.format(
            file_name=self.file_name, datetime=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        )
        
        # 行番号なしで出力
        log("log出力")
        try:
            df.to_csv(csv_path, index=False, encoding="utf-8-sig")
            return True
        except Exception as e:
            log(f"エラー内容: {e}")
            return False
        


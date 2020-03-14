#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import src.config_selenium

"""
    プログラム全体の説明
    実行方法とか必要なライブラリとか
    動作確認しているPythonのバージョンとか
"""


def main(url):
    """ エントリポイント

    """
    # ドライバーをインストール(と設定代入)
    driver = src.config_selenium.main()
    driver.get(url)
    archive_URL = "http://web.archive.org/save/"
    target_url = archive_URL + url
    driver.get(target_url)


if __name__ == "__main__":
    url_main = 'https://vdata.nikkei.com/newsgraphics/coronavirus-world-map/data/data.tsv'
    main(url_main)

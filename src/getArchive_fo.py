#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import src.config_selenium

"""
Archive.foの魚拓作成用プログラム
"""


def main(url):
    """ エントリポイント

    """
    # ドライバーをインストール(と設定代入)
    driver = src.config_selenium.main()

    # ブラウザの動作
    driver.get(url)
    archive_URL = "https://archive.fo/?run=1&amp;url="
    target_url = archive_URL + url
    driver.get(target_url)


if __name__ == "__main__":
    url_main = "https://vdata.nikkei.com/newsgraphics/coronavirus-world-map/data/data.tsv"
    main(url_main)

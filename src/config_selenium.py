#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from chromedriver_py import binary_path  # 自動でchromedriverインストールするモジュール
from selenium import webdriver

"""
seleniumの設定とインストール
"""


def main():
    """ エントリポイント

    """

    driver = webdriver.Chrome(executable_path=binary_path)
    return driver


if __name__ == "__main__":
    main()

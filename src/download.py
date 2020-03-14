#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import urllib.request


# データをダウンロード
def download(url: str, path: str, title: str, extension: str) -> str:
    file_name: str = "{path}{title}-{date}.{extension}".format(path=path, title=title, date=datetime.date.today(),
                                                               extension=extension)
    urllib.request.urlretrieve(url, file_name)
    return file_name


if __name__ == "__main__":
    url_main = 'https://vdata.nikkei.com/newsgraphics/coronavirus-world-map/data/data.tsv'
    path_main = '../data/'
    title_main = "data"
    extension_main = 'tsv'
    download(url_main, path_main, title_main, extension_main)

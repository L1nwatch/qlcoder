#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.12 学习一下没接触过的断点续传
"""
import requests

__author__ = '__L1n__w@tch'


def solve():
    url = "http://www.qlcoder.com/download/hugefile"
    header = {
        "Range": "bytes={}-{}".format(12345678901, 12345678999)
    }
    response = requests.get(url, headers=header)
    print(response.text)


if __name__ == "__main__":
    solve()

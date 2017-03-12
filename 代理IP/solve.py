#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.03.12 学习一下 requests 库的代理 IP 设置
"""
import requests

__author__ = '__L1n__w@tch'


def solve():
    url = "http://www.qlcoder.com/train/proxy"

    proxies = {
        'http': 'http://121.201.63.168:8080',
    }

    response = requests.get(url, proxies=proxies)

    print(response.text)


if __name__ == "__main__":
    solve()

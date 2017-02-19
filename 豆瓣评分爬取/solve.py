#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.19 要求爬 https://movie.douban.com/top250 拿下评分和
"""
import requests
import re
import gmpy2
from bs4 import BeautifulSoup

__author__ = '__L1n__w@tch'


def get_all_url(url):
    all_url = [url]

    response = requests.get(url)
    parse = BeautifulSoup(response.text)

    for each_tag in parse.find_all("a", href=re.compile("\?start=\d+.*"), text=re.compile("\d+")):
        all_url.append("{}{}".format(url, each_tag.attrs["href"]))
    return all_url


def crawl(url):
    result_sum = 0.0
    counts = 0

    # 首页
    all_url = get_all_url(url)

    # 对每页的分数进行提取
    for each_url in all_url:
        response = requests.get(each_url)
        parse = BeautifulSoup(response.text)
        result = parse.find_all("span", class_="rating_num")
        for each_move_tag in result:
            counts += 1
            result_sum += float(each_move_tag.contents[0])
            if counts == 166:
                print(result_sum)
                return None


if __name__ == "__main__":
    root_url = "https://movie.douban.com/top250"
    crawl(root_url)

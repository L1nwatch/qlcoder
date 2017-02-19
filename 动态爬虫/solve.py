#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.19 又一道爬虫题, 在自己 mac 上跑不出结果来就被禁了, 只好放 vps 跑了
"""
import requests
import time

__author__ = '__L1n__w@tch'


def get_frequency(url):
    # 初始间隔为 5 s
    frequency = 5.0
    first_time = True
    pre_content = requests.get(url).text

    # 检测 10 次
    for i in range(10):
        # 每次间隔 frequency 秒
        time.sleep(frequency)
        current_content = requests.get(url).text
        # 如果内容不等, 时间间隔下降 0.5 s
        if pre_content != current_content:
            frequency -= 0.5
            # 频率已经高到 0.5 s 内都有更新了, 直接返回吧
            if frequency < 0.5:
                break
        # 如果内容相等, 且是第一次访问, 不作处理
        elif first_time:
            first_time = False
        # 如果内容相等, 并且不是第一次, 则时间间隔加 0.5s:
        elif not first_time:
            frequency += 0.5

    return frequency


def old_solve():
    url = "http://www.qlcoder.com/train/spider3/{}"

    # 求出每个网页的频率
    frequency = dict()
    for each in range(1, 11):
        frequency[each] = get_frequency(url.format(each))

    print(frequency)
    # 然后排序
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1])

    # 得到答案
    # frequency = {1: 0, 2: 0, 3: 14, 4: 10, 5: 14, 6: 14, 7: 14, 8: 14, 9: 6, 10: 0}
    # 1-10-2-9-4-3-5-6-7-8
    # 提交说是不对...
    print("-".join([str(x[0]) for x in sorted_frequency]))


def has_change(order, pre_content):
    url = "http://www.qlcoder.com/train/spider3/{}"

    text = requests.get(url.format(order + 1)).text
    if pre_content[order] != text:
        pre_content[order] = text
        change_flag = True
    else:
        change_flag = False

    return change_flag


def solve():
    frequency_dict = dict()  # {1: 171, 2: 169, 3: 1, 4: 1, 5: 2, 6: 6, 7: 1, 8: 1, 9: 22, 10: 128}
    pre_content = [str() for x in range(10)]

    with open("result.txt", "w") as f:
        while True:
            for each in range(10):
                frequency_dict.setdefault(each + 1, 0)
                if has_change(each, pre_content):
                    frequency_dict[each + 1] += 1

            # 打印结果
            sorted_frequency = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
            print("[+] {}\t\t{}".format(frequency_dict, "-".join([str(x[0]) for x in sorted_frequency])),
                  file=f, flush=True)

            # 最小的结果都大于 3 的时候, 结束循环
            # if min(sorted_frequency, key=lambda x: x[1])[1] > 3:
            #     break

            # 每隔 5 s 进行一次
            time.sleep(5)


if __name__ == "__main__":
    # old_solve()
    solve()

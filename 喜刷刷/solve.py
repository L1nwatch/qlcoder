#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.27 多进程的逻辑有点问题, 需要跑的时间太长, 跑到明天所有验证码都得失效, 还是一边跑一边提交吧
2017.02.27 虽然用多进程试图提高效率, 但是觉得还应该从时间复杂度上优化算法
2017.02.27 解决一道喜刷刷的题目
"""
import datetime
import requests
import multiprocessing

try:
    import simplejson as json
except ImportError:
    import json

from functools import partial
from Crypto.Hash import MD5

__author__ = '__L1n__w@tch'


def return_infinitude_number():
    count = 0
    while True:
        yield count
        count += 1


def get_verify_code(current_num, check_codes):
    print("[*] 开始计算第 {} 票的验证码".format(current_num))
    today = datetime.datetime.today()
    hash_data = "{year}{month}{day}{username}{current_number}".format(year=today.year,
                                                                      month=str(today.month).zfill(2),
                                                                      day=str(today.day).zfill(2),
                                                                      username="w@tch",
                                                                      current_number=current_num)

    for i in return_infinitude_number():
        # md5(当天日期+你的用户名+当前的票数+x)
        if MD5.new("{}{}".format(hash_data, i).encode("utf8")).hexdigest().startswith("0" * 6):
            check_codes[current_num] = i
            print("[+] 获取到第 {} 票的验证码为: {}".format(current_num, i))
            return i


def solve_with_pool():
    """
    使用进程池
    """
    manager = multiprocessing.Manager()
    pool = multiprocessing.Pool(40)
    check_codes = manager.dict()

    # 获取从 1 到 1000 投每一票需要的验证码
    pool.map(partial(get_verify_code, check_codes=check_codes), [i for i in range(1, 1000 + 1)])

    # 保存一下验证码
    print(check_codes)
    check_codes = dict(check_codes)
    with open("result_check_code.txt", "w") as f:
        json.dump(check_codes, f)

    # 然后提交
    vote(check_codes)


def vote(check_codes):
    for i in range(1, len(check_codes)):
        url = ("http://www.qlcoder.com/train/handsomerank?_token=d4texP05ci7veIAztvnwe5yETOFhlLWkSaBYC51B"
               "&user=w%40tch&checkcode={}".format(check_codes[i]))
        response = requests.get(url)
        if response.status_code == 200:
            print("已经提交第 {} 票".format(i))


def solve_without_pool():
    """
    不使用进程池
    :return:
    """
    manager = multiprocessing.Manager()
    check_codes = manager.dict()

    # 获取从 1 到 1000 投每一票需要的验证码
    jobs = list()
    for i in range(1, 1000 + 1):
        p = multiprocessing.Process(target=get_verify_code, args=(i, check_codes))
        jobs.append(p)
        p.start()

    for process in jobs:
        process.join()

    print(check_codes)

    # 然后提交
    vote(check_codes)


def single_thread_solve():
    """
    发现就算用多进程算出所有验证码, 到了明天就失效了, 所以还是一个一个来吧
    """
    check_codes = dict()
    for i in range(82, 1000 + 1):
        # 获取从 1 到 1000 投每一票需要的验证码
        check_code = get_verify_code(i, check_codes)

        # 然后提交
        url = ("http://www.qlcoder.com/train/handsomerank?_token=d4texP05ci7veIAztvnwe5yETOFhlLWkSaBYC51B"
               "&user=w%40tch&checkcode={}".format(check_code))
        response = requests.get(url)
        if response.status_code == 200:
            print("已经提交第 {} 票".format(i))


if __name__ == "__main__":
    # solve_without_pool()
    # solve_with_pool()
    single_thread_solve()

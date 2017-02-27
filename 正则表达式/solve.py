#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.27 参考: http://www.qlcoder.com/task/7578, 编写一个正则进行匹配
"""
import re

__author__ = '__L1n__w@tch'


def solve(data):
    id_re = re.compile("\d{6}19(8[5-9]|9[0-4])\d{6}[13579][X\d]")
    if id_re.match(data):
        return True
    else:
        return False


if __name__ == "__main__":
    pass

#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 按照指定格式读取文件即可, 难度应该不大

题目链接: http://www.qlcoder.com/task/766e
"""
import binascii

__author__ = '__L1n__w@tch'


def solve():
    counts = 0
    with open("rf.data", "rb") as f:
        flag = f.read(1)
        # 2 表示接下来没有图片了
        while flag != b"\x02":
            size = f.read(4)
            # size 转 int
            picture_content = f.read(int(binascii.hexlify(size), 16))
            # 1 表示照片已经被删除了
            if flag == b"\x01":
                pass
            elif flag == b"\x00":
                # 0 表示照片可用
                counts += 1
                with open("{}.png".format(counts), "wb") as p:
                    p.write(picture_content)
            flag = f.read(1)


if __name__ == "__main__":
    solve()

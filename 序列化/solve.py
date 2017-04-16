#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 解决序列化的题目
"""
import serialize

__author__ = '__L1n__w@tch'


def solve():
    with open("145691935645609.data", "rb") as f:
        task = serialize.Task()
        task.parse_from_bytes(f.read())
        print(sum([each.data for each in task.answer]))


if __name__ == "__main__":
    solve()

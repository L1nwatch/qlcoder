#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 进行游程编码以及 BWT 的逆运算
"""
from itertools import zip_longest

__author__ = '__L1n__w@tch'

END = "|"


def ibwt(r):
    table = [''] * len(r)
    for _ in r:
        table = sorted([r[m] + table[m] for m in range(len(r))])
    s = [row for row in table if row.endswith(END)][0]
    return s.rstrip(END)


def divide_group(text, size):
    """
    对字符串进行分组操作
    :param text: "abcdefghi"
    :param size: 3
    :return: ["abc", "def", "ghi"]
    """
    assert len(text) % size == 0

    args = [iter(text)] * size
    for block in zip_longest(*args):
        yield "".join(block)


def de_rle(encoded_text):
    """
    游程编码逆运算, 好像是 run length encoding ?
    :param encoded_text: str(), 经过游程编码的字符串, 比如 "|1n4b3n2^1a9"
    :return: str(), 解码后的字符串, 比如 "|nnnnbbbnn^aaaaaaaaa"
    """
    result = str()
    for each_char, each_times in divide_group(encoded_text, 2):
        result += each_char * int(each_times)
    return result


def fast_de_rle(encoded_text):
    """
    加速的游程编码逆运算
    :param encoded_text: str(), 经过游程编码的字符串, 比如 "|1n4b3n2^1a9"
    :return: str(), 解码后的字符串, 比如 "|nnnnbbbnn^aaaaaaaaa"
    """
    result = str()
    pre_char = None
    is_times = False

    for each_char in encoded_text:
        if is_times:
            result += pre_char * int(each_char)
            is_times = False
        else:
            pre_char = each_char
            is_times = True
    return result


def solve(bwt_rle_text):
    # 先进行游程编码逆运算
    return ibwt(fast_de_rle(bwt_rle_text))


if __name__ == "__main__":
    assert "^bananabananabanana" == solve("|1n4b3n2^1a9")

    with open("144957540328740.txt", "r") as f:
        data = f.read().strip()

    print("[*] 开始进行 rle 逆运算")
    decode_rle = fast_de_rle(data)
    with open("rle_decoded.txt", "w") as f:
        f.write(decode_rle)

    print("[*] 开始进行 bwt 逆运算")
    with open("result.txt", "w") as f:
        f.write(ibwt(decode_rle))

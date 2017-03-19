#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 进行游程编码以及 BWT 的逆运算

参考: https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform
"""
from itertools import zip_longest

__author__ = '__L1n__w@tch'

END = "|"


def slow_inverse_bwt(r):
    table = [''] * len(r)
    for _ in r:
        table = sorted([r[m] + table[m] for m in range(len(r))])
    s = [row for row in table if row.endswith(END)][0]
    return s.rstrip(END)


def fast_inverse_bwt(r, *args):
    """Inverse Burrows-Wheeler transform. args is the original index if it was not indicated by an ETX character."""

    first_col = "".join(sorted(r))
    count = [0] * 256
    byte_start = [-1] * 256
    output = [""] * len(r)
    shortcut = [None] * len(r)
    # Generates shortcut lists
    for i in range(len(r)):
        shortcut_index = ord(r[i])
        shortcut[i] = count[shortcut_index]
        count[shortcut_index] += 1
        shortcut_index = ord(first_col[i])
        if byte_start[shortcut_index] == -1:
            byte_start[shortcut_index] = i

    local_index = (r.index("|") if not args else args[0])
    for i in range(len(r)):
        # takes the next index indicated by the transformation vector
        next_byte = r[local_index]
        output[len(r) - i - 1] = next_byte
        shortcut_index = ord(next_byte)
        # assigns local_index to the next index in the transformation vector
        local_index = byte_start[shortcut_index] + shortcut[local_index]
    return "".join(output).rstrip("|")


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
    return fast_inverse_bwt(fast_de_rle(bwt_rle_text))


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
        f.write(fast_inverse_bwt(decode_rle))

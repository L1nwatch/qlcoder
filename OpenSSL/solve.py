#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.03.12 解决一道密码学的问题
"""
from Crypto.Cipher import Blowfish

__author__ = '__L1n__w@tch'


def solve():
    bs = Blowfish.block_size
    key = b'qlcoder'
    with open("blowfish.data", "rb") as f:
        cipher_text = f.read()
    iv = cipher_text[:bs]
    cipher_text = cipher_text[bs:]

    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    msg = cipher.decrypt(cipher_text)

    # 解码失败
    print(msg)

    last_byte = msg[-1]
    msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]

    # 解码失败
    print(repr(msg))


if __name__ == "__main__":
    solve()

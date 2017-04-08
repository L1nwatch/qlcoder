#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 解决一道 RSA 的题目
"""
import gmpy2
import binascii

__author__ = '__L1n__w@tch'


def solve():
    cipher_text = "14a091645d307b8abd8632a1fb83f81e38c1b33d3286ca814a5742bec52c4b06d08"
    n = 41031587223377599579245988781518671358060455361860183212406274189493280555347897
    e = 65537
    # p 和 q 是用 yafu 这个工具分解得到的
    p = 6847944682037444681162770672798288913849
    q = 5991810554633396517767024967580894321153
    assert gmpy2.mpz(p) * gmpy2.mpz(q) == n
    d = gmpy2.invert(e, (p - 1) * (q - 1))
    plaintext = rsa_decrypt(int(cipher_text, 16), d, n)
    print(binascii.unhexlify(hex(plaintext)[2:]))


def rsa_decrypt(cipher_text, d, n):
    print("[*] Given c = {}, d = {}, n = {}".format(cipher_text, d, n))
    return gmpy2.powmod(cipher_text, d, n)


if __name__ == "__main__":
    solve()

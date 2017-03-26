#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 解决凯撒密码和栅栏密码的

[*] 最终结论: 自己的两种解法, 一种是栅栏密码, 另一种是 rail fence 都没有解决出来, 然后网上给的代码并不懂是什么解法
[*] 自己的栅栏密码应该是有问题的, 没时间弄了
"""
from rail_fence_cipher import NewZhaLan
import string
import random

__author__ = '__L1n__w@tch'


def solve():
    with open("cipher_text.txt", "r") as f:
        cipher_text = f.read()

    possible = dict()

    for i in range(1, len(cipher_text)):
        # plaintext = NewZhaLan(i).decrypt(cipher_text)
        plaintext = crack_transposition(cipher_text, i)
        possible[i] = plaintext

    for key, each_answer in possible.items():
        for each_char in string.punctuation:
            if each_answer.endswith(each_char):
                print("{} -> {}".format(key, each_answer))


def crack_transposition(cipher, msg_col_dim):
    msg_ch_arr = ['-' for n in range(len(cipher))]
    msg_row_dim = (len(cipher) + (msg_col_dim - 1)) // msg_col_dim

    idx_step = msg_row_dim - 1
    start_change_idx = (len(cipher) % msg_col_dim + 1) * msg_row_dim - 1

    for idx in range(0, len(cipher)):
        final_index = idx
        if final_index >= start_change_idx:
            final_index += (final_index - start_change_idx + idx_step) // idx_step
        msg_row_idx = final_index % msg_row_dim
        msg_col_idx = final_index // msg_row_dim
        msg_idx = msg_row_idx * msg_col_dim + msg_col_idx
        msg_ch_arr[msg_idx] = cipher[idx]

    return ''.join(msg_ch_arr)


if __name__ == "__main__":
    solve()

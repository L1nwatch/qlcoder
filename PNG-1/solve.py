#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 试着解析 png, 通过 crc32 判断是哪个 chunk 出错了
"""
import binascii

__author__ = '__L1n__w@tch'


def solve():
    """
    已经定位出是第 5 个 chunk 的 crc32 不对, 于是尝试修复
    :return:
    """
    with open("145682845224096.png", "rb") as f:
        # 单独读文件头
        header = binascii.hexlify(f.read(8))

        # 循环读取 4 个 chunk, 并校对 CRC32
        for i in range(4):
            length = f.read(4)  # 长度
            chunk_type_code = f.read(4)  # 数据块类型码
            chunk_data = f.read(int(binascii.hexlify(length), 16))
            crc = binascii.hexlify(f.read(4)).lstrip(b"0")  # CRC32

            print("[*] 读取第 {} 个 chunk, 长度为: {}".format(i + 1, binascii.hexlify(length)))

        # 修复第 5 个 chunk
        old_length = f.read(4)  # 图片给定的长度
        chunk_type_code = f.read(4)  # 数据块类型码
        offset = f.tell()  # 保存当前的位置
        for length in range(1, 2 ** 32 + 1):
            # 尝试读取
            chunk_data = f.read(length)
            crc = binascii.hexlify(f.read(4)).lstrip(b"0")  # CRC32
            # 计算 CRC32
            my_crc = str(hex(binascii.crc32(chunk_type_code + chunk_data))[2:]).encode().lstrip(b"0")

            if my_crc == crc:
                print("[*] 修复成功, 正确的 length 应该为: {}".format(hex(length)[2:]))
                break
            else:
                # 恢复到读取前的位置
                f.seek(offset)


def locate():
    """
    用来定位问题的
    :return:
    """
    with open("145682845224096.png", "rb") as f:
        # 单独读文件头
        header = binascii.hexlify(f.read(8))
        counts = 0

        # 循环读取 chunk, 并校对 CRC32, 直至 CRC32 校验不通过
        while True:
            counts += 1

            try:
                length = f.read(4)  # 长度
                if length == b"\x00\x00\x10\x00":
                    pass
                chunk_type_code = f.read(4)  # 数据块类型码
                chunk_data = f.read(int(binascii.hexlify(length), 16))
                crc = binascii.hexlify(f.read(4)).lstrip(b"0")  # CRC32
            except ValueError:
                print("[*] 文件读取完毕")
                break
            print("[*] 读取第 {} 个 chunk, 长度为: {}".format(counts, binascii.hexlify(length)))

            # 计算 CRC32
            my_crc = str(hex(binascii.crc32(chunk_type_code + chunk_data))[2:]).encode().lstrip(b"0")

            if my_crc != crc:
                print("[-] 自己计算得到的 CRC 是 {}, 图片给的 CRC 是 {}".format(my_crc, crc))
                raise RuntimeError("[-] CRC 校验出错")


if __name__ == "__main__":
    locate()
    # solve()

#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" BMP 格式的题目

题目链接: http://www.qlcoder.com/task/7659
BMP 图片格式:
参考 Wiki: https://zh.wikipedia.org/wiki/BMP#.E6.96.87.E4.BB.B6.E6.A0.BC.E5.BC.8F
"""
import binascii

__author__ = '__L1n__w@tch'


def byte2int(content):
    assert isinstance(content, bytes)
    return int.from_bytes(content, byteorder="little")


def parse_bmp_header(header_bytes):
    print("[*] {sep} 以下为 位图文件头 {sep}".format(sep="=" * 30))
    # 2 字节, 用于标识BMP和DIB文件的魔数，一般为0x42 0x4D, 即 BM
    flag = header_bytes[:2]
    print("[*] 标志位: {}".format(flag))

    # 4 字节, BMP文件的大小（单位为字节）
    size = header_bytes[2:2 + 4]
    print("[*] BMP 文件的大小(字节): {}".format(byte2int(size)))

    # 4 字节的保留值
    _ = header_bytes[6: 6 + 4]

    # 位图数据（像素数组）的地址偏移，也就是起始地址
    start_address = header_bytes[10:10 + 4]
    print("[*] 起始地址: {}".format(byte2int(start_address)))

    with open("result.bmp", "wb") as f:
        f.write(flag + size + _ + start_address)


def parse_dib_header(header_bytes):
    print("[*] {sep} 以下为 DIB 头 {sep}".format(sep="=" * 30))
    # 注意 DIB 头有 7 个版本, 本题为 BITMAPINFOHEADER
    # 该头结构的大小（本题为 40 字节）
    dib_header_size = header_bytes[:4]
    print("[*] DIB 头大小: {}".format(byte2int(dib_header_size)))

    # 位图宽度，单位为像素（有符号整数）
    width = header_bytes[4:4 + 4]
    print("[*] 位图宽度: {}".format(byte2int(width)))

    # 位图高度，单位为像素（有符号整数）
    height = header_bytes[8: 8 + 4]
    print("[*] 位图高度: {}".format(byte2int(height)))

    # 色彩平面数；只有1为有效值
    plane_num = header_bytes[12:12 + 2]
    print("[*] 色彩平面数: {}".format(byte2int(plane_num)))

    # 每个像素所占位数，即图像的色深。典型值为1、4、8、16、24和32
    color_deep = header_bytes[14:14 + 2]
    print("[*] 色深: {}".format(byte2int(color_deep)))
    color_deep = bytes.fromhex(hex(8)[2:].zfill(2)) + b"\x00"

    # 所使用的压缩方法, 值为 0 表示无压缩方法
    compress_method = header_bytes[16:16 + 4]
    print("[*] 压缩方法: {}".format(byte2int(compress_method)))

    # 图像大小
    picture_size = header_bytes[20:20 + 4]
    print("[*] 图像大小: {}".format(byte2int(picture_size)))

    # 图像的横向分辨率，单位为像素每米（有符号整数）
    horizontal_ppi = header_bytes[24:24 + 4]
    print("[*] 横向分辨率: {}".format(byte2int(horizontal_ppi)))

    # 图像的纵向分辨率，单位为像素每米（有符号整数）
    vertical_ppi = header_bytes[28:28 + 4]
    print("[*] 纵向分辨率: {}".format(byte2int(vertical_ppi)))

    # 调色板的颜色数，为0时表示颜色数为默认的2^色深个
    color_num = header_bytes[32:32 + 4]
    print("[*] 调色板颜色数: {}".format(byte2int(color_num)))

    # 重要颜色数，为0时表示所有颜色都是重要的；通常不使用本项
    important_color_num = header_bytes[36:36 + 4]
    print("[*] 重要颜色数: {}".format(byte2int(important_color_num)))

    with open("result.bmp", "ab") as f:
        f.write(dib_header_size + width + height + plane_num + color_deep +
                compress_method + picture_size + horizontal_ppi + vertical_ppi + color_num + important_color_num)

    return byte2int(color_num)


def parse_color_plane(header_bytes, limit):
    print("[*] {sep} 以下为 调色板 {sep}".format(sep="=" * 30))

    with open("result.bmp", "ab") as f:
        for i in range(0, limit):
            b, g, r, _ = header_bytes[i * 4: i * 4 + 4]
            print("[*] 第 {} 个调色板颜色为: b-{}, g-{}, r-{} ".format(i + 1, b, g, r))
            f.write(header_bytes[i * 4: i * 4 + 4])


def parse_ppi_array(header_bytes, limit):
    print("[*] {sep} 以下为 像素数组 {sep}".format(sep="=" * 30))

    with open("result.bmp", "ab") as f:
        first_byte = bin(int.from_bytes(header_bytes[:1], byteorder="big"))[2:]
        binary_stream = "0" * (8 - len(first_byte)) + bin(int.from_bytes(header_bytes, byteorder="big"))[2:]
        for each_chunk in chunks(binary_stream, 7):
            f.write(bytes.fromhex(hex(int(each_chunk, 2))[2:].zfill(2)))


def read_until_end(file):
    result = bytes()
    data = file.read()
    while data:
        result += data
        data = file.read()
    return result


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def solve():
    with open("145752260153647.bmp", "rb") as f:
        # 位图文件头 - 14 字节
        bmp_header = f.read(14)
        parse_bmp_header(bmp_header)

        dib_header_size = f.read(4)
        dib_header = f.read(byte2int(dib_header_size) - 4)
        color_num = parse_dib_header(dib_header_size + dib_header)

        color_plane = f.read(color_num * 4)
        parse_color_plane(color_plane, color_num)

        ppi_array = read_until_end(f)
        parse_ppi_array(ppi_array, color_num)


if __name__ == "__main__":
    solve()

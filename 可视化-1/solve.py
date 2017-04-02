#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 可视化

本来想研究 Matlab 的库的, 看了半天头好痛, 所以还是算了吧
"""
from PIL import Image

__author__ = '__L1n__w@tch'

if __name__ == "__main__":
    # 创建一张全黑的图
    img = Image.new('RGB', (1000, 1000), (0, 0, 0))
    px = img.load()
    with open('145035182953188.txt', 'r') as p:
        for line in p:
            point = line.split()
            # 设置像素点
            px[(int(point[0]), int(point[1]))] = (255, 255, 255)
    img.show()

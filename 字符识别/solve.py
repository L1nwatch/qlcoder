#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.12 又要学习光学识别库了, 试了 pyocr 库, 失败
"""
import pyocr
import math
import pyocr.builders
from PIL import Image
import tesserocr

__author__ = '__L1n__w@tch'


def old_solve():
    """
    pyocr 库识别, 识别率太低
    """
    tools = pyocr.get_available_tools()
    tool = tools[0]
    # Ex: Will use tool 'tesseract'
    print("Will use tool '%s'" % (tool.get_name()))

    language = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(language))
    language = language[1]
    # Ex: Will use lang 'fra'
    print("Will use language '%s'" % (language))

    for i in range(10001):
        picture = Image.open("cap1/im{}.png".format(i))
        txt = tool.image_to_string(picture, builder=pyocr.builders.TextBuilder())
        print(txt)


def same_old_solve():
    """
    识别率依旧很低, 不提了...
    """
    for i in range(10001):
        picture_path = "cap1/im{}.png".format(i)
        picture = Image.open(picture_path)
        result1 = tesserocr.image_to_text(picture.convert('L'), lang='eng')
        result2 = tesserocr.file_to_text(picture_path, psm=tesserocr.PSM.AUTO)
        print(result1)
        print(result2)


def find_rectangle_four_point(pixel_list):
    """
    找出矩形的四个点
    :param pixel_list: list(), [(x1, y1), (x2, y2), ...]
    :return: list(), [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], 为矩形的 4 个点
    """
    # 找出四个点
    x_min, y_min, x_max, y_max = 9999, 9999, -9999, -9999
    x_min_point, y_min_point, x_max_point, y_max_point = None, None, None, None
    for each_point in pixel_list:
        # x 最小
        if x_min > each_point[0]:
            x_min = each_point[0]
            x_min_point = each_point
        # x 最大
        if x_max < each_point[0]:
            x_max = each_point[0]
            x_max_point = each_point
        # y 最小
        if y_min > each_point[1]:
            y_min = each_point[1]
            y_min_point = each_point
        # y 最大
        if y_max < each_point[1]:
            y_max = each_point[1]
            y_max_point = each_point
    return [x_min_point, y_min_point, x_max_point, y_max_point]


def compute_length_width(four_point):
    """
    通过矩形的四个点计算长/宽
    :param four_point: list(), [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], 为矩形的 4 个点
    :return: tuple, (length, width), 计算得到的矩形长/宽
    """
    x_min_point, y_min_point, x_max_point, y_max_point = four_point

    width = ((x_min_point[0] - y_min_point[0]) ** 2 + (x_min_point[1] - y_min_point[1]) ** 2) ** 0.5
    length = ((x_min_point[0] - y_max_point[0]) ** 2 + (x_min_point[1] - y_max_point[1]) ** 2) ** 0.5

    return width, length


def compute_angle(width, length):
    answer = 18
    angle_result = (9999, None)
    for angle in range(-180, 180):
        denominator = 1 - 2 * (math.cos(angle) ** 2)
        numerator = width * math.sin(angle) - length * math.cos(angle)
        result = int(abs(numerator / denominator))

        sub = abs(result - answer)
        if sub < angle_result[0]:
            angle_result = (sub, angle)

    return angle_result[1]


def rotate_picture(picture):
    sizes = picture.size
    pixel_list = list()

    # 从左往右扫描
    for i in range(sizes[0]):
        # 从上往下扫描
        for j in range(sizes[1]):
            color = picture.getpixel((i, j))

            # 如果为黑色
            if color != (0, 0, 0):
                pixel_list.append((i, j))

    width, length = compute_length_width(find_rectangle_four_point(pixel_list))
    angle = compute_angle(width, length)
    picture = picture.rotate(angle)

    return picture


def solve():
    """
    先旋转再识别
    :return:
    """
    for i in range(10001):
        picture_path = "cap1/im{}.png".format(i)
        picture = Image.open(picture_path)
        picture = rotate_picture(picture)
        # picture.save("tmp.png")
        result1 = tesserocr.image_to_text(picture.convert("L"), lang="eng")
        picture.show()
        print(result1.strip())
        input("")


if __name__ == "__main__":
    # old_solve()
    # same_old_solve()
    solve()

#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.02.13 学习资料严重不足, 放弃了
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
        picture = online_rotate_picture(picture)
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

    width = ((x_max_point[0] - y_min_point[0]) ** 2 + (x_max_point[1] - y_min_point[1]) ** 2) ** 0.5
    length = ((x_max_point[0] - y_max_point[0]) ** 2 + (x_max_point[1] - y_max_point[1]) ** 2) ** 0.5

    return width, length


def compute_angle(width, length):
    """
    计算角度的方法一, 用的公式是
        18 = abs(
                height * sin(a) - width * cos(a)
                --------------------------------
                1 - 2 * cos(a) * cos(a)
                )
    不过这个公式算出来结果不准...
    :param width: int(), 矩形宽
    :param length: int(), 矩形长
    :return:  int(), 公式计算结果最接近 18 的 a 值
    """
    answer = 15
    angle_result = (9999, None)
    for angle in range(-360, 360):
        radians = math.radians(angle)
        denominator = 1 - 2 * (math.cos(radians) ** 2)
        numerator = width * math.sin(radians) - length * math.cos(radians)
        result = abs(numerator / denominator)

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


def online_rotate_picture(image):
    """
    网上的答案, 旋转图片用的
        对原始图片进行旋转修正及其他增强
    :param image:
    :return:
    """
    # 获取图片内容的包围盒。返回包围盒左上角和右下角的坐标
    box = image.getbbox()
    width = box[2] - box[0]
    height = box[3] - box[1]
    # print('图片包围盒{}，宽{}，高{}'.format(box, width, height))

    # 获取包围盒上沿的包围，以确定旋转的方向
    region = image.crop((box[0], box[1], box[2], box[1] + 1))
    box2 = region.getbbox()
    mid = width / 2
    if box2[0] < mid < box2[2]:
        # 图像是完全平直的 不需要旋转
        return image
    adjacent = max(box2[0], width - box2[2])  # 邻边
    # print('邻边包围盒{}，边长{}'.format(box2, adjacent))

    # 获取包围盒左边缘的包围，确定旋转的角度
    region = image.crop((box[0], box[1], box[0] + 1, box[3]))
    box3 = region.getbbox()
    opposite = max(box3[1], height - box3[3])  # 对边
    # print('对边包围盒{}，边长{}'.format(box3, opposite))

    import math
    angle = math.atan(opposite / adjacent) / math.pi * 180

    if box2[0] > mid:
        # 图像经过逆时针旋转。需要对其进行顺时针旋转才能还原
        angle = - angle
    # print('补偿旋转角度{}'.format(int(angle)))

    # 放大
    size = image.size
    ret = image.resize((size[0] * 2, size[1] * 2), Image.ANTIALIAS)

    # 旋转
    ret = ret.rotate(angle)

    # 亮度增强，以强化被放大模糊了的边缘
    from PIL import ImageEnhance
    ret = ImageEnhance.Contrast(ret)
    ret = ret.enhance(2)

    # 切边
    ret = ret.crop(ret.getbbox())

    # box = image.getbbox()
    # width = box[2] - box[0]
    # height = box[3] - box[1]
    # print('图片包围盒{}，宽{}，高{}'.format(box, width, height))

    return ret


def solve():
    """
    先旋转再识别
    :return:
    """
    for i in range(10001):
        picture_path = "cap1/im{}.png".format(i)
        picture = Image.open(picture_path)
        # picture = rotate_picture(picture)
        picture = online_rotate_picture(picture)
        result1 = tesserocr.image_to_text(picture.convert("L"), lang="eng")
        # picture.show()
        print(result1.strip())


if __name__ == "__main__":
    # old_solve()
    # same_old_solve()
    solve()

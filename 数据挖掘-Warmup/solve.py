#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 第一次尝试数据挖掘的题目

没看到啥好资料, 也没时间从 0 开始学数据挖掘, 直接学讨论区的代码吧
"""
import numpy
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing

__author__ = '__L1n__w@tch'

work_type = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay',
             'Never-worked']

education_type = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th',
                  '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']

marry_type = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent',
              'Married-AF-spouse']

occupation_type = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial',
                   'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing',
                   'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']

role_type = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']

race_type = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']

gender_type = ['Female', 'Male']

nationality_type = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany',
                    'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba',
                    'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal',
                    'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia',
                    'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador',
                    'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']

type_list = [work_type, education_type, marry_type, occupation_type, role_type, race_type, gender_type,
             nationality_type]


def transform(data_ele):
    data_ele = data_ele.decode()
    if data_ele.isdigit():
        # 是数字的话直接返回 int()
        return int(data_ele)
    elif data_ele == "?":
        # 未知数据直接返回 -1
        return -1
    else:
        # 不是的话返回索引值
        for each_type in type_list:
            if data_ele in each_type:
                return each_type.index(data_ele)
        raise RuntimeError("[-] 存在异常数据: {}".format(data_ele))


def solve():
    # 加载训练数据以及测试数据
    training_arr = numpy.loadtxt('adult.txt', dtype=bytes, comments='#', delimiter=',')
    test_data = numpy.loadtxt('adult_test.txt', dtype=bytes, comments='#', delimiter=',')

    # 初始化 x 值数组和 y 值数组, 貌似没啥用
    # x_list = numpy.ndarray(len(training_arr))
    # y_list = numpy.ndarray(len(training_arr))

    # 把收入当做 y 值
    y_list = [int(element[12]) for element in training_arr]
    # 除收入外, 其他数值都作为 x 值
    x_list = [[transform(x) for x in element[0:12]] for element in training_arr]
    # 创建测试数据
    test_data = [[transform(x) for x in element] for element in test_data]

    assert isinstance(y_list[0], int)  # y 列表的每个值是 0 或 1, 即 int
    assert len(x_list[0]) == 12  # x 列表总共有 12 个元素, 分别表示 12 个相关因素
    assert len(test_data[0]) == 12  # 测试数据同 x 列表

    clf = GaussianNB()
    clf.partial_fit(x_list, y_list, numpy.unique(y_list))  # clf.fit(x_list, y_list) 效果一样啊
    res_arr = clf.predict(test_data)
    partial_fit_result = "".join([str(x) for x in res_arr])

    print("[*] 最终预测结果: {}".format(partial_fit_result))


if __name__ == "__main__":
    solve()

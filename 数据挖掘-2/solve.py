#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 再次尝试数据挖掘, 不自己写了, 用 autosklearn

"""
import numpy
# import autosklearn.classification
from sklearn.naive_bayes import GaussianNB

__author__ = '__L1n__w@tch'

if __name__ == "__main__":
    # 加载训练数据以及测试数据
    training_arr = numpy.loadtxt('train.txt', dtype=bytes, comments='#', delimiter=' ')
    test_data = numpy.loadtxt('check.txt', dtype=bytes, comments='#', delimiter=' ')

    # 把收入当做 y 值
    y_list = [int(element[11]) for element in training_arr]
    # 除收入外, 其他数值都作为 x 值
    x_list = [[float(x) for x in element[1:11]] for element in training_arr]
    # 创建测试数据
    test_data = [[float(x) for x in element[1:11]] for element in test_data]

    assert isinstance(y_list[0], int)
    assert len(x_list[0]) == 10
    assert len(test_data[0]) == 10

    print(y_list[0])
    print(x_list[0])
    print(test_data[0])

    clf = GaussianNB()
    clf.partial_fit(x_list, y_list, numpy.unique(y_list))  # clf.fit(x_list, y_list) 效果一样啊
    res_arr = clf.predict(test_data)
    partial_fit_result = "".join([str(x) for x in res_arr])

    print("[*] 最终预测结果: {}".format(partial_fit_result))

    # cls = autosklearn.classification.AutoSklearnClassifier()
    # cls.fit(x_list, y_list)
    # predictions = cls.predict(test_data)

    # print("[*] 最终预测结果: {}".format(predictions))

#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 学习 rpc - thrift 相关知识点

题目链接: http://www.qlcoder.com/task/7698
"""
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from task7698 import Task
from task7698 import ttypes

__author__ = '__L1n__w@tch'


def solve():
    # Make socket
    transport = TSocket.TSocket("121.201.63.168", 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Task.Client(protocol)

    # Connect!
    try:
        transport.open()

        auth = ttypes.Auth()
        auth.username = "w@tch"
        auth.type = ttypes.Type.GET_ANSWER

        response = client.getTaskInfo(auth)
        print(response)
    finally:
        transport.close()


if __name__ == "__main__":
    solve()

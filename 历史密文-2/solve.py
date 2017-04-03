#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 试着写一下加密解密的题目吧, 虽然不太喜欢

2017.04.03 跑了半天没跑出来, 还是改一下代码然后放到服务器上跑吧
参考讨论区的 c 解法实现 python 解法吧
"""
import string

__author__ = '__L1n__w@tch'


def encrypt(keys, text):
    bytes_list = [ord(c) for c in text]
    result_str = ""
    for i in range(0, len(bytes_list), 3):
        temp = 0
        for j in range(3):
            temp <<= 8
            temp += bytes_list[i + j]
        for j in range(3):
            temp ^= (keys[temp & 3] << 8)
            temp = (temp << 7) | (temp >> 17)
            temp &= ((1 << 24) - 1)
        result_str += format(temp, '06x')
    return result_str


def decrypt(keys, cipher_text):
    """
    解密的密钥数组
    :param keys: list(), 比如 [11, 22, 33 ,44]
    :param cipher_text: str(), 加密后的 16 进制流, 比如 "5b0dcfc68c8d58e9c5680e4c"
    :return: str(), 解密后的结果, 比如 "hello,world!"
    """
    result_list = [int() for j in range(len(cipher_text) // 2)]

    for i in range(0, len(cipher_text), 6):
        temp = int(cipher_text[i:i + 6], 16)
        for j in range(3):
            temp &= (1 << 24) - 1
            temp = (temp << 17) | (temp >> 7)
            temp ^= keys[temp & 3] << 8
        result_list[i // 2] = (temp & 0xff0000) >> 16
        result_list[i // 2 + 1] = (temp & 0xff00) >> 8
        result_list[i // 2 + 2] = (temp & 0xff)
        # 参考讨论区, 增加了个判断, 如果存在不可打印字符则直接结束
        for j in range(3):
            if chr(result_list[i // 2 + j]) not in string.printable:
                return ""

    return "".join([chr(each) for each in result_list])


def example():
    key = [11, 22, 33, 44]  # key数组是byte数组,元素的取值范围是0-255
    plaintext = "hello,world!"
    ans = encrypt(key, plaintext)
    my_answer = decrypt(key, ans)
    print(ans)
    print(decrypt(key, ans))
    assert plaintext == my_answer


def generate_key():
    for i in range(256):
        for j in range(256):
            for x in range(256):
                for y in range(256):
                    yield [i, j, x, y]


def solve():
    cipher_text = "bb2af286e3ec8ead77cf81d0e7299fef8fd0a3837a4621fef3827dd0887c51aa168b4f0953aa3f070dfffc2cb0df8afdbdacbddce28165efe57ceac945cde63c28d23ce6e927a9f2624b4f8683fa51e8683da6fdaba13a2b055d0b2f7e0583f299081139027275089311cc6b112a124f85d3070dff6b237d53aa1f51805ed3aa3efd66e4dce2eb50ea29870dfffe26f4e66988116041b12073dda2f71d2292e381305ce28baf8dd3c643e1f92c90b1a45f1c86d6190e700ba932838d7794205669c54591205329eb468683fac9095e85c3cc51e868d1a05e6a4b4b8683fabb2af286e3ece9e546d02e504f85d36b0b5f6aa532bdacbde38530dce2e1130a12254fc8e9213751e868eb2137b1406ca72dff4601ff4aaf32a3837ad38a1f71827d7024139d22da5f64c56769c962215e0bab721340447c88fe5da29dd8805e6a412b6b237f590e33d16c464aaf327904132f89f0fc8adea589d2e8a550f50ed2250fdedcca814d095f990a334643a8ddaafdd0887ceb21175ca2bfd1a05ea9eb46d0887cc723d7bd28b2caaf30bf86ffdce2eb7faadfff46e45ce28b1f42a54603ff750eb305079658c2ab2ba313072dff6b237d53aa1f7f66e5d1c04fbfaeded1a05ab4267a152a12ea4361caaf324601ff6b2b5d8683fa1ca4dea6a9f2a60fdd690b5fd1aa3e5de280af89d28be925c643a1c5c5c6e729dcd90c50c723d73c2ad2ea21371d22923508923d2ad0d34e46620b5d8683fa71a05d8b2f3d3c2a92190830536c659ca4dc91281370827d7e26f3eb4b4bd0887ceb211705e3e61f84deeb6121d36c4490005245ede406a3f33d86fe074deb502e50620b5d71a05d53aa1f3508d2d3887ed0805fc643c167299ff0a0775ca2bf5da2d64f85d3d1805ffd8a9f50c82951805e7cea892a255e050dff6b237d53aa1fff66e6e9233ef50ed023813045c5c4b1ac5edfa2fd4aaf324f85d3870dfdbcee887daad63c4ae55f04d3e7618fbfaeded1a05ab4267a152a12ea4361aaa13abd2a92a6a9d227c9c4790413a3837a7ccae8ebc5467904122381536ba77250ea08936044c643c1716405d3887eea41216a237d53aa1f750e937ccac92a47608f85d33da6ff27a9f2b50ab2a9eb4586a3b3f08077930a12102a32870dffc4adf0fdaa9e7daabfa9c12c256fe80e0dffea610149095f438f5385e1ccc585d0df8ad7918e5d916a0507c3e48f81d33da6ff27a9f2a589d292205245ede4dfa2971d22926385533deec94aaf3258c04ca7a991af89d306e3e48f81d3bda6ffe5cfc67f06f2a9c366e68fd2936044c643c18b4f09e92137dce2814621fef3827dd0887c0727b649095f4f85d33f6aa4934045ff66e331426650ea4929c366702413604bce"

    # 生成 key
    for i, each_key in enumerate(generate_key()):
        print("[*] 第 {} 次尝试, 总共 {} 次".format(i + 1, 256 ** 4))

        # 执行解密操作
        plaintext = decrypt(each_key, cipher_text)

        # 判断是否解密成功
        if plaintext != "":
            with open("solve_result.txt", "a") as f:
                f.write("[*] key: {}, plaintext: {}\n".format(each_key, plaintext))


if __name__ == "__main__":
    solve()

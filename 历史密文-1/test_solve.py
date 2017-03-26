#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 自己写的栅栏破解居然失败了, 得试一下原因在哪
"""
import unittest
import string
import random
from rail_fence_cipher import NewZhaLan, RailFence

__author__ = '__L1n__w@tch'


class TestRailFence(unittest.TestCase):
    # def test_right_answer(self):
    #     with open("cipher_text.txt", "r") as f:
    #         test_data = f.read()
    #
    #     right_answer = "G iovnkx oy g skgty ul iutikgrotm g skyygmk, cnkxk rkzzkxy ul znk skyygmk gxk yahyzozazkj ux zxgtyvuykj lux uznkx rkzzkxy, rkzzkx vgoxy, gtj yuskzosky lux sgte rkzzkxy. Ot ixevzumxgvne, g irgyyoigr iovnkx oy g zevk ul iovnkx zngz cgy aykj noyzuxoigrre haz tuc ngy lgrrkt, lux znk suyz vgxz, otzu joyayk. Ot mktkxgr, irgyyoigr iovnkxy uvkxgzk ut gt grvnghkz ul rkzzkxy, gtj gxk osvrksktzkj he ngtj ux cozn yosvrk skingtoigr jkboiky. Znke gxk vxuhghre znk suyz hgyoi zevky ul iovnkxy, cnoin sgjk znks tuz bkxe xkroghrk, kyvkiogrre glzkx tkc zkinturume cgy jkbkruvkj. Sujkxt yinksky ayk iusvazkxy ux uznkx jomozgr zkinturume, gtj uvkxgzk ut hozy gtj hezky. Sgte irgyyoigr iovnkxy ckxk aykj he ckrr xkyvkizkj vkuvrk, yain gy Paroay Igkygx gtj Tgvurkut, cnu ixkgzkj znkox uct iovnkxy cnoin ckxk znkt vuvargxre aykj. Sgte iovnkxy ngj znkox uxomoty ot znk sorozgxe gtj ckxk aykj lux zxgtyvuxzotm ykixkz skyygmky gsutm vkuvrk ut znk ygsk yojk. Znk gtyckx sayz hk IrgyyoigrIxevzumxgvne. Irgyyoigr yinksky gxk ulzkt yayikvzohrk zu iovnkxzkdz utre gzzgiqy, yuskzosky kbkt coznuaz qtucrkjmk ul znk yeyzks ozykrl, ayotm zuury yain gy lxkwaktie gtgreyoy. Yuskzosky mxuavkj cozn irgyyoigr iovnkxy gxk suxk gjbgtikj skingtoigr ux krkizxu skingtoigr iovnkx sginotky, yain gy znk Ktomsg sginotk."
    #
    #     for i in range(2, len(test_data)):
    #         rf = RailFence()
    #         my_answer = rf.decode(test_data, i)
    #         if my_answer.endswith("."):
    #             print(my_answer)
    #             self.assertTrue(my_answer.endswith("."))

    def test_rail_fence_cipher(self):
        """
        原来我写的是栅栏密码而不是 rail fence 密码
        :return:
        """
        test_data = "WECRLTEERDSOEEFEAOCAIVDEN"
        wiki_answer = "WEAREDISCOVEREDFLEEATONCE"
        rf = RailFence()
        my_answer = rf.decode(test_data, 3)
        self.assertEqual(wiki_answer, my_answer)
        my_answer = rf.encode(wiki_answer, 3)
        self.assertEqual(test_data, my_answer)

    def test_my_zha_lan(self):
        test_data = "WRIORFEOEEESVELANADCEDETC   adsadasdsadsa"
        right_answer = "WEA aRED sISC dOVEasREDdaFLEsdEATasONCdaE"
        my_answer = NewZhaLan(5).decrypt(test_data)
        self.assertEqual(right_answer, my_answer)

        test_data = "WRIORFEOEEESVELANADCEDETC   "
        right_answer = "WEVDTROECCIELE OEAD RENE FSA"
        my_answer = NewZhaLan(5).decrypt(test_data)
        self.assertEqual(right_answer, my_answer)

    def test_encode_with_two_rails(self):
        rf = RailFence()
        self.assertMultiLineEqual(
            rf.encode('XOXOXOXOXOXOXOXOXO', 2), 'XXXXXXXXXOOOOOOOOO')

    def test_encode_with_three_rails(self):
        rf = RailFence()
        self.assertMultiLineEqual(
            rf.encode('WEAREDISCOVEREDFLEEATONCE', 3),
            'WECRLTEERDSOEEFEAOCAIVDEN')

    def test_encode_with_middle_stop(self):
        rf = RailFence()
        self.assertMultiLineEqual(rf.encode('EXERCISES', 4), 'ESXIEECSR')

    def test_decode_with_three_rails(self):
        rf = RailFence()
        self.assertMultiLineEqual(
            rf.decode('TEITELHDVLSNHDTISEIIEA', 3), 'THEDEVILISINTHEDETAILS')

    def test_decode_with_five_rails(self):
        rf = RailFence()
        self.assertMultiLineEqual(
            rf.decode('EIEXMSMESAORIWSCE', 5), 'EXERCISMISAWESOME')

    def test_decode_with_six_rails(self):
        rf = RailFence()
        self.assertMultiLineEqual(
            rf.decode(
                '133714114238148966225439541018335470986172518171757571896261',
                6),
            '112358132134558914423337761098715972584418167651094617711286')

    def test_average_divide_group(self):
        test_data = "WRIORFEOEEESVELANADCEDETC   adsadasdsadsa"
        right_answer = [
            ['W', 'R', 'I', 'O', 'R', 'F', 'E', 'O', 'E'],
            ['E', 'E', 'S', 'V', 'E', 'L', 'A', 'N', ],
            ['A', 'D', 'C', 'E', 'D', 'E', 'T', 'C', ],
            [' ', ' ', ' ', 'a', 'd', 's', 'a', 'd', ],
            ['a', 's', 'd', 's', 'a', 'd', 's', 'a', ]
        ]
        my_answer = NewZhaLan(5).average_divide_group(test_data, 9)
        self.assertEqual(right_answer, my_answer)


if __name__ == "__main__":
    pass

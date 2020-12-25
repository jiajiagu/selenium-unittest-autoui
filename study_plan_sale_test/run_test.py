#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/22 10:54 下午
# @Author  : jiajia.gu
import sys, os
import unittest,HTMLTestRunner
from study_plan_sale_test.TestCase import Level1toLevel2,Level1toLevel3,Level1toLevel4,Level3toLevel4,Level3toLevel5

sys.path.append(os.path.join(os.path.dirname(__file__), "."))
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "TestCase"))



if __name__ == "__main__":
    Lv1ToLV2 = unittest.TestLoader().loadTestsFromTestCase(Level1toLevel2.Lv1ToLV2)
    Lv1ToLV3 = unittest.TestLoader().loadTestsFromTestCase(Level1toLevel3.Lv1ToLV3)
    Lv1ToLV4 = unittest.TestLoader().loadTestsFromTestCase(Level1toLevel4.Lv1ToLV4)
    LV3ToLV4=unittest.TestLoader().loadTestsFromTestCase(Level3toLevel4.Lv3ToLV4)
    LV3ToLV5 = unittest.TestLoader().loadTestsFromTestCase(Level3toLevel5.Lv3ToLV5)
    suite = unittest.TestSuite([
                                Lv1ToLV2,Lv1ToLV3,Lv1ToLV4,LV3ToLV4,LV3ToLV5
                                ])
    outfile = open("./study_plan_test.html", "wb")
    testRunner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Study Plan Test Report',
                                               description='This is The Study Plan Test report')
    testRunner.run(suite)
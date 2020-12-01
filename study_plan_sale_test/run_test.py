#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/22 10:54 下午
# @Author  : jiajia.gu
import sys, os
from selenium import webdriver
import time
from selenium.webdriver.common.touch_actions import TouchActions
import unittest,HTMLTestRunner
from TestCase import Level1toLevel2,Level1toLevel3

sys.path.append(os.path.join(os.path.dirname(__file__), "."))
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "TestCase"))



if __name__ == "__main__":
    Lv1ToLV2 = unittest.TestLoader().loadTestsFromTestCase(Level1toLevel2.Lv1ToLV2)
    Lv1ToLV3 = unittest.TestLoader().loadTestsFromTestCase(Level1toLevel3.Lv1ToLV3)

    suite = unittest.TestSuite([
                                Lv1ToLV2,Lv1ToLV3
                                ])
    outfile = open("./study_plan_test.html", "wb")
    testRunner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Study Plan Test Report',
                                               description='This is The Study Plan Test report')
    testRunner.run(suite)
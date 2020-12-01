#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/22 11:16 下午
# @Author  : jiajia.gu
import sys, os
from selenium import webdriver
from TestCase import *
import time
from selenium.webdriver.common.touch_actions import TouchActions
import unittest
class Lv1ToLV2(unittest.TestCase):
    def setUp(self):
        u'''没有前置条件可以写pass'''
        print("开始执行")
        # pass

    def test01(self):  # 测试用例必须以test开头
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})  # '模拟iphoneX'
        driver = webdriver.Chrome(options=options)
        driver.get('https://sprout-hybrid.liulishuo.com/wx/study-plan-guide?from=free')
        time.sleep(5)
        driver.find_elements_by_class_name("guide-btn")[0].click()
        time.sleep(5)
        driver.find_elements_by_class_name("ph-button")[0].click()#选择字母
        time.sleep(5)
        driver.find_elements_by_class_name("ph-button")[2].click()#选择单词
        time.sleep(5)
        driver.find_elements_by_class_name("ph-button")[1].click()#选择句子
        time.sleep(5)
        # driver.TouchActions.scroll("am-picker-col-mask", 0, +200).perform()
        driver.find_elements_by_class_name("study-plan-bt-btn")[0].click()  # 选择完年龄点击完成水平测试
        time.sleep(5)
        driver.find_elements_by_class_name("imager-inner")[2].click()#点击定制专属学习计划
        time.sleep(5)
        driver.find_elements_by_class_name("select-item")[1].click()#选择期望提升
        time.sleep(5)
        # driver.find_elements_by_class_name("ph-button")[1].click()
        # time.sleep(5)
        driver.find_elements_by_class_name("imager-inner")[0].click()#点击底部button
        time.sleep(5)
        driver.find_elements_by_class_name("ph-button")[1].click()#选择学习时间
        time.sleep(5)
        driver.find_elements_by_class_name("imager-inner")[0].click()#点击底部button
        time.sleep(15)
        self.assertEqual(driver.find_elements_by_class_name("study-target__item-content")[0].get_attribute('innerHTML'),
                         u'Lv.2', msg='失败')

    def tearDown(self):
        u'''没有后置条件可以写pass'''
        print("结束...")


if __name__ == "__main__":
    unittest.main()


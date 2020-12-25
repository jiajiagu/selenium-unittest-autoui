#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/12/3 6:57 下午
# @Author  : jiajia.gu
import unittest
from selenium.webdriver.common.touch_actions import TouchActions
from study_plan_sale_test.config.config import url3
from study_plan_sale_test.common.common import *
from study_plan_sale_test.page.studyPlanPage import StudyPlan
from selenium import webdriver
import time



class Lv3ToLV4(unittest.TestCase):

    def setUp(self):
        u'''没有前置条件可以写pass'''
        print("开始执行")
        # pass

    def test_Level(self):  # 测试用例必须以test开头
        freeSalePage_url = url3
        driver=get_url(freeSalePage_url)
        page = StudyPlan(driver)
        chooseStudyInfo(page)
        time.sleep(3)
        # driver.TouchActions.scroll("am-picker-col-mask", 0, +200).perform()
        element1 = driver.find_elements_by_class_name("am-picker-col-indicator")[0]
        # element2 = driver.find_elements_by_class_name("am-picker-col-indicator")[1]
        time.sleep(3)

        TouchActions(driver).long_press(element1)
        TouchActions(driver).flick_element(element1,0,300,10).perform()
        time.sleep(3)
        page.study_plan_bt_btn_loc()[0].click()  # 选择完年龄点击完成水平测试
        time.sleep(5)
        page.imager_inner_loc()[2].click()  # 点击定制专属学习计划
        time.sleep(5)
        page.select_item_loc()[1].click()  # 选择期望提升
        time.sleep(5)

        get_sale_page(page)
        startingLevel=page.study_target_item_content_loc()[0].get_attribute('innerHTML')
        targetingLevel=page.study_target_item_content_loc()[1].get_attribute('innerHTML')
        self.assertEqual(startingLevel, u'Lv.3', msg='失败') # 验证起始等级为lv3
        self.assertEqual(targetingLevel, u'Lv.4', msg='失败')# 验证目标等级为lv4

    def tearDown(self):
        u'''没有后置条件可以写pass'''
        print("结束...")

    if __name__ == "__main__":
        unittest.main()


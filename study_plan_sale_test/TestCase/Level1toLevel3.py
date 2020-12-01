#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/30 10:36 下午
# @Author  : jiajia.gu
import unittest

from config.config import url3
from common.common import *
from page.studyPlanPage import StudyPlan


class Lv1ToLV3(unittest.TestCase):

    def setUp(self):
        u'''没有前置条件可以写pass'''
        print("开始执行")
        # pass

    def test_Level(self):  # 测试用例必须以test开头
        freeSalePage_url = url3
        driver=get_url(freeSalePage_url)
        page = StudyPlan(driver)
        chooseStudyInfo(page)
        # driver.TouchActions.scroll("am-picker-col-mask", 0, +200).perform()
        page.study_plan_bt_btn_loc()[0].click()  # 选择完年龄点击完成水平测试
        time.sleep(5)
        page.imager_inner_loc()[2].click()  # 点击定制专属学习计划
        time.sleep(5)
        page.select_item_loc()[2].click()  # 选择期望提升
        time.sleep(5)

        page.imager_inner_loc()[0].click()  # 点击底部button
        time.sleep(5)
        page.ph_button_loc()[1].click()  # 选择学习时间
        time.sleep(5)
        page.imager_inner_loc()[0].click()  # 点击底部button
        time.sleep(15)
        startingLevel=driver.find_elements_by_class_name("study-target__item-content")[0].get_attribute('innerHTML')
        targetingLevel=driver.find_elements_by_class_name("study-target__item-content")[1].get_attribute('innerHTML')
        self.assertEqual(startingLevel, u'Lv.1', msg='失败') # 验证起始等级为lv1
        self.assertEqual(targetingLevel, u'Lv.3', msg='失败')# 验证目标等级为lv3

    def tearDown(self):
        u'''没有后置条件可以写pass'''
        print("结束...")

    if __name__ == "__main__":
        unittest.main()


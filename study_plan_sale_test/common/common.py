#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/23 11:40 下午
# @Author  : jiajia.gu


import os
path=os.getcwd()
from selenium import webdriver

import time

#获得url流程封装
def get_url(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})  # '模拟iphoneX'
    options.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    return driver

#选择学习基础流程封装
def chooseStudyInfo(page):

    page.guide_btn_loc()[0].click()
    time.sleep(5)
    page.ph_button_loc()[0].click()  # 选择字母
    time.sleep(5)
    page.ph_button_loc()[2].click()  # 选择单词
    time.sleep(5)
    page.ph_button_loc()[1].click()  # 选择句子
    time.sleep(10)

def get_sale_page(page):
    page.imager_inner_loc()[0].click()  # 点击底部button
    time.sleep(5)
    page.ph_button_loc()[1].click()  # 选择学习时间
    time.sleep(5)
    page.imager_inner_loc()[0].click()  # 点击底部button
    time.sleep(15)
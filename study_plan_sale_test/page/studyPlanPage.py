#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/24 11:48 下午
# @Author  : jiajia.gu
from selenium import webdriver
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def class_name(self, class_name):
        return self.driver.find_elements_by_class_name(class_name)

class StudyPlan(BasePage):
    def guide_btn_loc(self):
        return self.class_name("guide-btn")

    def ph_button_loc(self):
        return self.class_name("ph-button")

    def study_plan_bt_btn_loc(self):
        return self.class_name("study-plan-bt-btn")

    def imager_inner_loc(self):
        return self.class_name("imager-inner")

    def select_item_loc(self):
        return self.class_name("select-item")

    def am_picker_col_indicator_loc(self):
        return self.class_name("am-picker-col-indicator")

    def study_target_item_content_loc(self):
        return self.class_name("study-target__item-content")
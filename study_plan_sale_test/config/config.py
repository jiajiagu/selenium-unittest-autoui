#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/11/24 12:02 上午
# @Author  : jiajia.gu
import configparser
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))

cf = configparser.ConfigParser()
cf.read(parent_dir + "/config.ini")

url1 = cf.get("Urls", "url1")
url2 = cf.get("Urls", "url2")
url3 = cf.get("Urls", "url3")
url4 = cf.get("Urls", "url4")

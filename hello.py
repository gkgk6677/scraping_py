# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://naver.com')
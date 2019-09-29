# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://naver.com')

# F12 관리자 모드에 들어가서 로그인 버튼을 선택 후 xpath로 복사하여 경로값 넣어준다.
element = Select(driver.find_element_by_xpath("//*[@id='account']/div/a"))
driver.execute_script("arguments[0].click();")
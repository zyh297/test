'''百度搜索
1、找到输入框，输入关键词
2、点击【百度一下】按钮搜索'''

from selenium import webdriver
from selenium import time

#1、打开网页
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("http://www.baidu.com")

#2、找到输入框，输入关键词
driver.find_element_by_name('wd').send_keys("中国机长")
time.sleep(2)

#3、点击【百度一下】按钮搜索
driver.find_element_by_id('su').click()
time.sleep(2)

#4、点击搜索结果
driver.find_element_by_link_text('中国机长(中国2019年刘伟强执导电影)_百度百科').click()
time.sleep(2)

driver.forward()
time.sleep(2)
driver.find_element_by_name("kw").send_keys("足球")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.find_element_by_partial_link_text("百度").click()
time.sleep(2)

driver.quit()



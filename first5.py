from selenium import webdriver  #引入webdriver
import time                     #引入时间
driver = webdriver.Chrome()     #访问浏览器
driver.maximize_window()          #窗口最大化
from selenium.webdriver.common.by import By    #引入By

url = "http://localhost/upload/index.php"     #浏览器地址
driver.get(url=url)      #访问ecshop页面
time.sleep(2)            #停留2秒

driver.find_element_by_xpath('/html/body/div[1]/div/div/font/a[1]').click()   #点击登录
time.sleep(2)                                                                 #停留2秒

driver.find_element_by_name("username").send_keys("zyh")          #找到输入框并输入用户名zyh
driver.find_element_by_name("password").send_keys("zyh123456")    #找到输入框输入密码zyh123456
time.sleep(2)                                                      #停留2秒
driver.find_element_by_name("submit").click()                     #找到登录按钮并点击
time.sleep(3)                                                     #停留3秒

driver.find_element_by_class_name("a").click()                  #找到首页按钮并点击
time.sleep(2)                                                   #停留2秒
driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[3]/div/form/div/div/a/img').click()           #点击商品
time.sleep(2)                                                     #停留2秒
driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]/div[2]/form/ul[3]/li[2]/a/img').click()    #点击立即购买
time.sleep(2)                                                     #停留2秒
driver.find_element_by_xpath('/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img').click()              #点击结算中心
time.sleep(2)                                                      #停留2秒
# driver.find_element_by_id("selProvinces_0").send_keys("四川")      #输入省份
# driver.find_element_by_id("selCities_0").send_keys("成都")         #输入市成都
# driver.find_element_by_id("selDistricts_0").send_keys("锦江区")     #输入区级名
# driver.find_element_by_id("consignee_0").send_keys("张小花")        #输入收货人姓名
# driver.find_element_by_id("address_0").send_keys("锦江区")          #输入详细地址
# driver.find_element_by_id("tel_0").send_keys("123456")             #输入电话号码
# time.sleep(2)                                                      #停留2秒
# driver.find_element_by_class_name("bnt_blue_2").click()            #点击配送至这个地址
# time.sleep(2)                                                      #停留2秒
driver.find_element_by_xpath('/html/body/div[7]/form/div[11]/div[2]/input[1]').click()   #点击提交订单
time.sleep(2)                                                     #停留2秒
driver.quit()                                                     #退出

from selenium import webdriver        #引入webdriver
import time                           #引入时间
driver = webdriver.Chrome()           #访问浏览器
driver.maximize_window()              #浏览器页面最大化
from selenium.webdriver.common.by import By   #引入By

url = "http://localhost/upload/admin/privilege.php?act=login"   #浏览器地址
driver.get(url=url)                        #访问ecshop页面

driver.find_element_by_name("username").send_keys("root")          #找到输入框并输入用户名zyh
driver.find_element_by_name("password").send_keys("zyh123456")    #找到输入框输入密码zyh123456
time.sleep(2)                                                     #停留2秒
driver.find_element_by_class_name("button").click()               #点击进入管理中心

driver.switch_to.frame("menu-frame")                              #进入左侧菜单栏
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[3]').click()  #点击订单管理
time.sleep(2)                                                              #停留2秒
driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[3]/ul/li[2]/a').click()  #点击订单查询
time.sleep(2)                                                      #停留2秒
driver.switch_to.parent_frame()                                    #返回上一层
driver.switch_to.frame("main-frame")                               #进入右侧页面

driver.find_element_by_id("order_sn").send_keys("2020071611126")    #搜索订单号
driver.find_element_by_id("query").click()                 #点击搜索
time.sleep(5)                                                       #停留2秒
driver.quit()                                                       #退出
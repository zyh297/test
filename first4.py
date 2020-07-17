from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
from selenium.webdriver.common.by import By                           #引入By


driver.get("http://www.jd.com")                                       #访问京东页面
time.sleep(2)
#业务操作
#搜索
driver.find_element_by_id("key").send_keys("华为手机")                 #找到输入框输入华为手机
driver.find_element_by_xpath('//button[@class="button"]').click()     #点击
time.sleep(2)
handles = driver.window_handles             #获取所有窗口的句柄
driver.switch_to.window(handles[-1])         #跳转窗口

driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img').click()    #点击第二个商品
time.sleep(2)
handles = driver.window_handles             #获取所有窗口的句柄
driver.switch_to.window(handles[-1])         #跳转窗口

print(driver.current_url)
price = driver.find_element(By.XPATH,'//span[@class="p-price"]/span[2]').text     #获取标签的文本
print("价格",price)                                #打印价格

driver.find_element(By.ID,'InitCartUrl').click()   #加入购物车
time.sleep(2)
handles = driver.window_handles             #获取所有窗口的句柄
driver.switch_to.window(handles[-1])         #跳转窗口

print(driver.current_url)                   #打印当前页面地址
driver.find_element_by_id('key').clear()    #清楚内容

print(driver.title)
driver.quit()
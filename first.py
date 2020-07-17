#webdriver 浏览器控制说明#
from selenium import webdriver
import time

driver = webdriver.Chrome()         #启动浏览器
driver.maximize_window()            #窗口最大化
driver.get("http://www.baidu.com")  #打开浏览器并访问百度
time.sleep(2)
driver.refresh()                    #刷新页面

driver.set_window_size(800,1000)    #800,1000为窗口大小
driver.get("http://www.taobao.com")
time.sleep(5)
driver.refresh()

driver.get("http://www.jd.com")       #访问京东
time.sleep(3)                         #停留3秒
driver.back()                         #返回
time.sleep(3)                         #等待3秒
driver.forward()                      #前进

driver.close()                        #关闭页面
driver.quit()                         #结束任务并退出进程
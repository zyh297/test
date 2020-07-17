from selenium import webdriver         #引入webdriver
driver = webdriver.Chrome()            #启动浏览器
river.maximize_window()               #窗口最大化
url = "http://www.taobao.com"          #淘宝url地址
driver.get(url=url)


driver.find_element_by_xpath('//input[@id="q"]').send_keys("女装")
time.sleep(2)
driver.find_element_by_css_selector('.btn-search tb-bg').click()


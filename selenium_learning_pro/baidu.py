import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http:www.baidu.com')

driver.find_element_by_id('kw').send_keys("selenium")
time.sleep(3)
driver.find_element_by_id('su').click()
driver.quit()




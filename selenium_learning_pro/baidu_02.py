"""
浏览器的等待
"""
from time import sleep,ctime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://www.baidu.com")


# element = WebDriverWait(driver,timeout=5,poll_frequency=0.5).until(EC.presence_of_element_located((By.ID,'kw')))
# element.send_keys("selenium")
# #通过回车键代替单击的操作
# time.sleep(3)
# driver.find_element_by_id("su").send_keys(Keys.ENTER)
# time.sleep(5)
# driver.quit()



# 可以通过is_dispalyed方法判断元素是否可见

# print(ctime())
#
# for i in range(10):
#     try:
#         e1 = driver.find_element_by_id("kw")
#         if e1.is_displayed():
#             break
#     except:pass
#     sleep(1)
# else:
#     print("time out")
# driver.close()
# print(ctime())


# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from time import ctime
#
# driver = webdriver.Firefox()
#
# # 设置显示等待
# driver.implicitly_wait(10)
# driver.get("http://wwww.baidu.com")
#
# try:
#     print(ctime())
#     driver.find_element_by_id("kw22").send_keys('selenum')
# except NoSuchElementException as e:
#     print(e)
# finally:
#     print(ctime())
#     driver.quit()



# 设置显示等待

from  selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

sleep(5)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('webdriver')
driver.find_element_by_id('su').click()
sleep(2)

driver.quit()


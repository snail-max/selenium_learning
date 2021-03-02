from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
"""
常用的键盘操作
    send_keys(Keys.BACK_SPACE)  #删除键
    send_keys(Keys.SPACE)   # 空格键
    send_keys(Keys.TAB)   制表键（tab）
    send_keys(Keys.ESCAPE)  回退键
    send_keys(Keys.ENTER)  回车键 enter
    
    
    
         """

# 输入输入框的内容
driver.find_element_by_id("kw").send_keys("selenium")

#删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#输入空格键 + “教程“
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")


# ctrl + a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')


# ctrl + x 剪切输入框的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")

time.sleep(1)
#ctrl + v 黏贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

#通过回车键代替单击的操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()

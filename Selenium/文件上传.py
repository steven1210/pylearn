import time
from selenium import webdriver
import win32com.client

'''
对于通过 input 实现的文件上传，我们可以将其看作是一个输入框。即通过 send_keys 的方式即可实现文件上传

对于非 input 标签实现的上传功能，我们可以通过模拟键盘敲击的方式去实现
'''
url = 'http://tinypng.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# 1，定位到文件上传的 input 标签
# ele = driver.find_element_by_css_selector("input[type=\"file\"]")
# ele.send_keys("D:\\pylearn\\Selenium\\0.jpg")

# 2，对于非 input 标签通过模拟键盘敲击的方式上传文件
# 点击 文件上传 按钮
time.sleep(5)
ele = driver.find_element_by_css_selector("figure.icon")
ele.click()
time.sleep(5)
# 模拟键盘敲击，只有执行到这里就会点击
sh = win32com.client.Dispatch("WScript.shell")
# 模拟输入，\r\n是模拟回车
sh.SendKeys("D:\\pylearn\\Selenium\\0.jpg\r\n")
# 退出浏览器
driver.quit()

"""
1, 代码运行过程中不要操作鼠标
2，输入法要保持英文输入的状态
"""

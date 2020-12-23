from selenium import webdriver
import time

url = 'http://127.0.0.1:8088/login'
# 创建浏览器驱动对象，打开浏览器
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()
# 访问网址
driver.get(url)
# 隐式等待2s
driver.implicitly_wait(5)
# 登录:输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 登录：输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 登录：点击登录按钮登录
driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
# 点击“项目管理”
driver.find_element_by_xpath("//ul[@class=\"nav nav-pills nav-stacked custom-nav js-left-nav\"]/li[2]//span").click()
# 点击“新项目”
time.sleep(3)
driver.find_element_by_xpath("//a[@class=\"btn btn-success\"]").click()
time.sleep(3)
# 输入“项目名称”
driver.find_element_by_xpath("//input[@name=\"name\"]").send_keys("项目管理与OA办公")
# 输入“项目别名”
driver.find_element_by_name("aliasname").send_keys("OPMS")
# 选择开始时间
# driver.find_element_by_name("started").click()
# 定位iframe
edit_frame = driver.find_element_by_css_selector(".ke-edit-iframe")
# 切换frame
driver.switch_to.frame(edit_frame)
# 输入描述内容
driver.find_element_by_css_selector("body.ke-content").send_keys("selenium测试")
# 切换到主页面
driver.switch_to.default_content()
# 点击提交按钮
driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
# 退出浏览器
driver.quit()

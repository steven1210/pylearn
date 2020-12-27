from selenium import webdriver
import pprint

'''
cookie 是服务端存在我们本地客户端的一些信息
并且是不涉及隐私的信息（这个通常要程序员自我约束）
cookie里边要存那些内容也不是固定的，完全按照 
'''
url = 'http://127.0.0.1:8088/login'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# 登录:输入用户名
driver.find_element_by_name("username").send_keys("libai")
# 登录：输入密码
driver.find_element_by_name("password").send_keys("opmsopms123")
# 登录：点击登录按钮登录
driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
# 获取所有的cookie信息
cookie_list = driver.get_cookies()
# 格式化打印
pprint.pprint(cookie_list)
# 获取某个cookie
# cookie = driver.get_cookie('beegosessionID')
# pprint.pprint(cookie)
driver.quit()

from selenium import webdriver

'''
获取到的断言信息就是实际结果
预期结果是我们确定的，直接写在代码中的
而实际结果是无法确定的，所以需要一些方法去获取实际结果信息
'''
url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# 1，获取当前页面的标题
title = driver.title
print(title)

# 2，获取当前页面的url
url = driver.current_url
print(url)

# 3，获取标签对之间的文本信息
# 3.1，标签元素如果不展示在页面上，获取结果为空
# 3.2，如果标签对中间没有值，获取到的结果也是空的
# 3.3，如果input之类的单标签，获取结果也是空的
title_text = driver.find_element_by_class_name("title-text").text
print(title_text)

# 4，获取元素属性
ele = driver.find_element_by_id("kw")
print(ele.get_attribute("class"))

# 退出浏览器
driver.quit()

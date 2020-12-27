import time
from selenium import webdriver
from selenium.webdriver.support.select import Select  # 导入下拉框支持包

url = 'D:\\pylearn\\Selenium\\dropdownbox.html'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# 定位下拉框元素
ele = driver.find_element_by_id("abc")
# 1，根据 下拉框文本 定位元素
# Select(ele).select_by_visible_text("月薪三千")

# 2，根据 下标 定位元素；下标从0开始
# Select(ele).select_by_index(2)

# 3，根据 value属性 定位元素
Select(ele).select_by_value("p4")

time.sleep(3)
# 退出浏览器
driver.quit()

from selenium import webdriver

url = 'D:\\pylearn\\Selenium\\test.html'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# 匹配元素列表，返回所有能匹配的元素，存放在一个列表中
ele_title = driver.find_elements_by_css_selector("div>ul>li")
for ele in ele_title:
    print(ele.text)


# 退出浏览器
driver.quit()

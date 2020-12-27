from selenium import webdriver

url = 'D:\\pylearn\\Selenium\\test.html'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# 1，根据 id 属性定位元素：只返回找到的第1个元素
ele = driver.find_element_by_id("abc").text
print(ele)

# 2，根据 name 属性定位元素：只返回找到的第1个元素
ele = driver.find_element_by_name("ab1").text
print(ele)

# 3，根据 链接文本 定位元素，精确匹配，链接文本必须写全：只返回找到的第1个元素
ele = driver.find_element_by_link_text("点击一下，进入百度")
print(ele.text)

# 4，根据 链接文本模糊匹配 定位元素，链接文本不用写全：只返回找到的第1个元素
ele = driver.find_element_by_partial_link_text("点击一下")
print(ele.text)

# 5，根据 tag_name 定位元素：只返回找到的第1个元素
ele = driver.find_element_by_tag_name("span")
print(ele.text)

# 6，根据 class 属性定位元素：只返回找到的第1个元素
ele = driver.find_element_by_class_name("ab2")
print(ele.text)

# 7，根据 xpath 定位元素：只返回找到的第1个元素
ele = driver.find_element_by_xpath("//div/ul/li[2]")
print(ele.text)

# 8，根据 css 定位元素：只返回找到的第1个元素
ele = driver.find_element_by_css_selector("html>body>div>ul>li:nth-child(3)")
print(ele.text)

# 退出浏览器
driver.quit()

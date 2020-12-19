from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait

url = 'https://m.weibo.cn/'
# 创建浏览器驱动对象，打开浏览器
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()
# 访问网址
driver.get(url)
# 隐式等待2s
driver.implicitly_wait(2)
# 点击搜索框
ele = driver.find_element_by_xpath("//div[@class=\"m-text-cut\"]")
ele.click()
# 点击“微博热搜榜”
ele = driver.find_element_by_xpath("//div[@class=\"card m-panel card16 m-col-2\"]//div[@class=\"m-item-box\"][8]//h4")
ele.click()
# 找到所有的实时热点
real_time_hots = driver.find_elements_by_xpath("//div[@class=\"card card11\"][1]//div[@class=\"card-list\"]/div/div/div"
                                               )
for real_time_hot in real_time_hots:
    # 获取实时热点的热点图标信息
    link_icon = real_time_hot.find_elements_by_xpath(".//span[@class=\"m-link-icon\"]/img")
    link_name = real_time_hot.find_element_by_xpath(".//span[@class=\"main-text m-text-cut\"]").text
    if link_icon:  # 判断热点图标不为空
        # 获取图片标签src的属性
        link_attribute = link_icon[0].get_attribute("src")
        if "hot" in link_attribute:  # 判断热搜类型
            # 设置热点名称
            link_type = "热"
            # 获取热搜文本
            # link_name = real_time_hot.find_element_by_xpath(".//span[@class=\"main-text m-text-cut\"]").text
            # 打印结果
            print(f'{link_name}：{link_type}')
        elif "new" in link_attribute:  # 判断热搜类型
            # 设置热点名称
            link_type = "新"
            # 获取热搜文本
            # link_name = real_time_hot.find_element_by_xpath(".//span[@class=\"main-text m-text-cut\"]").text
            # 打印结果
            print(f'{link_name}：{link_type}')
        elif "fei" in link_attribute:  # 判断热搜类型
            # 设置热点名称
            link_type = "沸"
            # 获取热搜文本
            # link_name = real_time_hot.find_element_by_xpath(".//span[@class=\"main-text m-text-cut\"]").text
            # 打印结果
            print(f'{link_name}：{link_type}')
        elif "jian" in link_attribute:  # 判断热搜类型
            # 设置热点名称
            link_type = "荐"
            # 获取热搜文本
            # link_name = real_time_hot.find_element_by_xpath(".//span[@class=\"main-text m-text-cut\"]").text
            # 打印结果
            print(f'{link_name}：{link_type}')
# 退出浏览器
driver.quit()

from selenium import webdriver  # 引入webdriver类
from selenium.webdriver.common.action_chains import ActionChains  # 引入ActionChains类

url = 'https://www.vmall.com/'
# 创建浏览器驱动对象，打开浏览器
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()
# 访问网址
driver.get(url)
# 隐式等待2s
driver.implicitly_wait(2)
# 获取所有的一级菜单
category_list = driver.find_elements_by_xpath("//ol[@class=\"category-list\"]/li")
# 获取每一个一级菜单的名称
for category in category_list:
    # 获取每一个一级菜单的名称
    category_name = category.find_element_by_xpath(".//div[@class=\"category-info\"]//span").text
    print("一级菜单：", category_name)
    # 打开二级菜单页面
    ActionChains(driver).move_to_element(category.find_element_by_xpath(".//div[@class=\"category-info\"]"))\
        .perform()
    # 获取每一个一级菜单里面的二级菜单
    sub_category_list = category.find_elements_by_xpath(".//ul[@class=\"subcate-list clearfix\"]/li["
                                                        "@class=\"subcate-item\"]")
    for sub_category in sub_category_list:
        sub_category_name = sub_category.find_element_by_xpath(".//span").text
        print("\t", sub_category_name)
# 退出浏览器
driver.quit()

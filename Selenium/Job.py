from selenium import webdriver
import time

url = 'http://www.51job.com'
# 创建浏览器驱动对象，打开浏览器
driver = webdriver.Chrome()
# 最大化浏览器
driver.maximize_window()
# 访问网址
driver.get(url)
# 隐式等待2s
driver.implicitly_wait(5)
# 点击“高级搜索”
driver.find_element_by_xpath("//a[@class=\"more\"]").click()
# 输入关键字
driver.find_element_by_xpath("//p[@class=\"ipt\"]/input[@id=\"kwdselectid\"]").send_keys("python")
# 选择地区
driver.find_element_by_id("work_position_input").click()
time.sleep(5)
# 找到已选择城市区域
work_position_selected = driver.find_element_by_id("work_position_click_multiple_selected")
# 获取已选择的城市列表
work_position_list = driver.find_elements_by_class_name("ttag")
for work_position in work_position_list:
    # 关闭已选择的城市
    work_position.click()
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
driver.find_element_by_id("work_position_click_bottom_save").click()
# 选择职能类别
driver.find_element_by_xpath("//div[@class=\"rtit r1\"]").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@class=\"txt pointer\"]/span[@id=\"funtype_click\"]").click()
driver.find_element_by_id("funtype_click_center_right_list_category_0100_0100").click()
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_0106").click()
time.sleep(2)
driver.find_element_by_id("funtype_click_bottom_save").click()
# 选择行业类别
time.sleep(5)
driver.find_element_by_xpath("//span[@id=\"indtype_click\"]").click()
driver.find_element_by_id("indtype_click_center_right_list_category_01_01").click()
time.sleep(2)
driver.find_element_by_id("indtype_click_bottom_save").click()
# 选择工作年限
driver.find_element_by_xpath("//div[@id=\"workyear_list\"]/span[@class=\"ic i_arrow\"]").click()
driver.find_element_by_xpath("//div[@id=\"workyear_list\"]//div[@class=\"ul\"]/span[3]").click()
# 点击搜索
driver.find_element_by_xpath("//div[@class=\"btnbox p_sou\"]/span[@class=\"p_but\"]").click()
# 获取工作列表
job_list = driver.find_elements_by_xpath("//div[@class=\"j_joblist\"]/div")
for job in job_list:
    # 获取职位名称
    job_name = job.find_element_by_xpath(".//span[@class=\"jname at\"]").text
    # 获取发布时间
    job_time = job.find_element_by_xpath(".//span[@class=\"time\"]").text
    # 获取公司名称
    company_name = job.find_element_by_xpath(".//a[@class=\"cname at\"]").text
    # 获取工资
    salary = job.find_element_by_xpath(".//span[@class=\"sal\"]").text
    # 获取地址信息
    address_info = job.find_element_by_xpath(".//span[@class=\"d at\"]").text
    # 从地址信息中获取地址
    address = address_info.split(' | ')[0]
    # 打印招聘信息
    print(f'{job_name} | {company_name} | {address} | {salary} | {job_time}')
# 退出浏览器
driver.quit()

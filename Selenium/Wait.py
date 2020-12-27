from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素模块
from selenium.webdriver.support import expected_conditions as EC  # 场景判断模块


url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

'''
方式一：硬等待：必须过了XXX毫秒以后才执行后面的命令
'''
# time.sleep(3) ele = driver.find_element_by_xpath("//a[@class=\"title-content c-link c-font-medium
# c-line-clamp1\"]//span[@class=\"title-content-title\"][1]") print(ele.text) driver.quit()

'''
方式二：隐式等待：
申明隐式等待，只对声明之后的代码有效。隐式等待默认参数是：秒。
当执行大某个元素定位时，能定位到就继续执行。若在最大等待时间内定位到元素了，就不等待了，继续执行。
若在最大等待时间内没有定位到元素，就抛出异常。
'''
# # driver.implicitly_wait(3) ele = driver.find_element_by_xpath("//a[@class=\"title-content c-link c-font-medium
# c-line-clamp1\"]//span[@class=\"title-content-title\"][1]") print(ele.text) driver.quit()

'''
方式三：显示等待
每隔0.5s轮询检查元素一次，最大等待时间5s；
若在最大等待时间内定位到元素了，就不等待了，继续执行。
若在最大等待时间内没有定位到元素，就抛出异常。
'''
ele = WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//a[@class=\"title-content c-link c-font-medium c-line-clamp1\"]//span["
                   "@class=\"title-content-title\"][1]")
    )
)
print(ele.text)
driver.quit()

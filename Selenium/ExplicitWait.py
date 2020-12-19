from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 封装显示等待方法
def explicitWaiting(self, ele, driver, timeout, poll_frequency, by, str_element):
    ele = WebDriverWait(driver, timeout, poll_frequency).until(
        EC.visibility_of_element_located(
            (by, str_element)
            )
    )

    return ele

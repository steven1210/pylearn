from POType.VersionTwo.myDriver import Driver
from POType.VersionTwo.settings import time_out, poll_time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = Driver.get_driver("Chrome")

    """
    显示等待，查找元素
    :param： locator:要求传入的参数是一个元组，表示元素定位方法和表达式
    :return：单个的元素对象
    """
    def get_element(self, locator):
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 设置超时时间
            timeout=time_out,
            # 设置轮询时间
            poll_frequency=poll_time
        ).until(EC.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)

    """
    显示等待，查找元素
    :param： locator:要求传入的参数是一个元组，表示元素定位方法和表达式
    :return：元素列表
    """
    def get_elements(self, locator):
        WebDriverWait(
            # 传入浏览器对象
            driver=self.driver,
            # 设置超时时间
            timeout=time_out,
            # 设置轮询时间
            poll_frequency=poll_time
        ).until(EC.visibility_of_element_located(locator))

        return self.driver.find_elements(*locator)

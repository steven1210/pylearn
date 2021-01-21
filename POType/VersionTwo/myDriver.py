from selenium import webdriver
from POType.VersionTwo.settings import driverPath, url

'''
任何地方需要用到浏览器驱动对象，直接调用此类下的 get_driver 函数，获取返回值即可
且get_driver 函数保证了我们的driver唯一
'''


class Driver:
    # 初始化为空
    driver = None

    @classmethod
    def get_driver(cls, browser_name):
        # 如果cls.driver为None，则证明不存在，进入if代码块去创建
        # 如果cls.driver不为None，则证明村子，不需要进入if代码块创建，可直接返回
        if cls.driver is None:
            if browser_name == "Chrome":
                cls.driver = webdriver.Chrome(driverPath["Chrome"])
            elif browser_name == "Firefox":
                cls.driver = webdriver.Firefox(driverPath["Firefox"])
            # 最大化浏览器窗口
            cls.driver.maximize_window()
            # 访问默认网页
            cls.driver.get(url)
        # 返回
        return cls.driver


# 测试get_driver方法
# if __name__ == '__main__':
#     Driver.get_driver("Chrome")

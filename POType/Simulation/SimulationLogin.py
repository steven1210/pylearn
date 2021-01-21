from POType.Simulation.settings import cookie_list
from POType.Simulation.myDriver import Driver


class SimulationLogin:
    # 获取浏览器驱动对象,并打开网页
    def __init__(self):
        self.driver = Driver.get_driver("Chrome")

    # 设置cookie
    def get_cookie(self):
        self.driver.delete_all_cookies()
        for cookie in cookie_list:
            # 添加cookie
            self.driver.add_cookie(cookie)
        self.driver.refresh()


if __name__ == '__main__':
    simulationLogin = SimulationLogin()
    simulationLogin.get_cookie()

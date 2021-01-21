import time
from POType.PrimaryVersion.myDriver import Driver
from POType.PrimaryVersion.settings import userName, password


class LoginPage:
    def __init__(self):
        # 创建浏览器驱动对象，打开浏览器
        self.driver = Driver.get_driver("Chrome")

    def user_name(self):  # 用户名
        return self.driver.find_element_by_name("username")

    def pass_word(self):  # 密码
        return self.driver.find_element_by_name("password")

    def login_button(self):  # 登录按钮
        return self.driver.find_element_by_css_selector("button")


'''
我们一般会将页面当中一些常用的动作，会重复使用的动作抽离出来，写成一个个函数，封装在一个页面动作当中
页面动作类，继承对应的页面类
'''


class LoginPageAction(LoginPage):
    def login(self):
        self.driver.refresh()
        self.user_name().send_keys(userName)
        self.pass_word().send_keys(password)
        self.login_button().click()
        time.sleep(3)
        self.driver.quit()


# 自测方法
if __name__ == '__main__':
    login = LoginPageAction()
    login.login()

"""
将页面分为： 页面元素类 与 页面动作类
若以后，只是逻辑修改，只需要改动动作类即可，而不必关心元素定位
若是元素定位发生了变化，只需要修改元素定位即可，执行动作、逻辑都不用关心
"""
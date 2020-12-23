from selenium import webdriver


# 页面登录类
class LoginPage:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)

    def user_name(self):  # 用户名
        return self.driver.find_element_by_name("username")

    def pass_word(self):  # 密码
        return self.driver.find_element_by_name("password")

    def login_button(self):  # 登录按钮
        return self.driver.find_element_by_css_selector("button")

    def login(self):
        self.user_name().send_keys("libai")
        self.pass_word().send_keys("opmsopms123")
        self.login_button().click()
        self.driver.quit()


login = LoginPage("http://127.0.0.1:8088/login")
login.login()

from selenium import webdriver
import time

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

driver = webdriver.Chrome(chrome_options=option)
driver.get('http://www.baidu.com')
time.sleep(3)
driver.quit()

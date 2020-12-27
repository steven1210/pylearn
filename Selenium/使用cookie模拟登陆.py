from selenium import webdriver

'''
cookie 是服务端存在我们本地客户端的一些信息
并且是不涉及隐私的信息（这个通常要程序员自我约束）
cookie里边要存那些内容也不是固定的，完全按照 
'''
url = 'http://127.0.0.1:8088/login'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# 使用cookie模拟登陆，需要先清空cookie
driver.delete_all_cookies()
# 使用cookie登陆，需要把cookie加入进去；但是每次只会增加1个字典，所以需要for循环，把所有的cookie添加进去
# 注意需要注释掉里面的过期时间
cookie_list = [{'domain': '127.0.0.1',
  'httpOnly': False,
  'name': 'Hm_lpvt_750463144f16fe69eb3ac11bea1c4436',
  'path': '/',
  'secure': False,
  'value': '1609076491'},
 {'domain': '127.0.0.1',
  # 'expiry': 1640612491,
  'httpOnly': False,
  'name': 'Hm_lvt_750463144f16fe69eb3ac11bea1c4436',
  'path': '/',
  'secure': False,
  'value': '1609076491'},
 {'domain': '127.0.0.1',
  # 'expiry': 1640612490,
  'httpOnly': True,
  'name': 'beegosessionID',
  'path': '/',
  'secure': False,
  'value': '541457e2b7996ff9fdfe55b72ff211d4'}]

for cookie in cookie_list:
    # 添加cookie
    driver.add_cookie(cookie)
# 添加cookie后，页面打开时还是未登陆状态，所以需要在添加cookie后，刷新一次
driver.refresh()
# 退出浏览器
driver.quit()

from CookieLearn.config.Config import HOST, course_list, user_info
from CookieLearn.lib.LoginClass import LoginClass
import requests

class Course:
    def course(self, courseData, inCookies):
        url = f'{HOST}/api/mgr/sq_mgr/'
        # 接口是返回cookie的值，这里可以同时将sessionid和token同时传入，解决双重鉴权
        in_cookie = {'sessionid': inCookies, 'token':'login'}
        payload = courseData
        resp = requests.get(url, params=payload, cookies=in_cookie)
        # 设置响应编码，解决响应体出现编码不是中文问题
        resp.encoding = 'unicode_escape'
        return resp.text


if __name__ == '__main__':
    inCookie = LoginClass().login(user_info, getCookie=False)
    res = Course().course(course_list, inCookie)
    print(res)

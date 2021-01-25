from CookieLearn.config.Config import HOST, course_list, user_info
from CookieLearn.lib.LoginClass import LoginClass
import requests

class CourseList:
    def courseList(self, courseData,inCookie):
        url = f'{HOST}/api/mgr/sq_mgr/'
        payload = courseData
        resp = requests.get(url, params=payload, cookies=inCookie)
        # 设置响应编码，解决响应体出现编码不是中文问题
        resp.encoding = 'unicode_escape'
        return resp.text


if __name__ == '__main__':
    inCookie = LoginClass().login(user_info, getCookie=True)
    res = CourseList().courseList(course_list, inCookie)
    print(res)

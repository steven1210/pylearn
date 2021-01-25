from CookieLearn.config.Config import HOST, user_info
import requests

class LoginClass:
    def login(self, userInfo, getCookie=False):
        url = f'{HOST}/api/mgr/loginReq'
        payload = userInfo
        resp = requests.post(url, data=payload)
        if getCookie:
            return resp.cookies  # 返回cookies对象
        else:
            return resp.cookies['sessionid']  # 返回cookie值


if __name__ == '__main__':
    res = LoginClass().login(user_info,getCookie=False)
    print(res)
import requests
from PyInterface.config.Config import HOST, login_info
from PyInterface.lib.EnCrypt import Encrypt

# 封装登录类
class Login:
    # 1，封装登录函数
    # 2，通过getToken来控制是否返回token
    def login(self, inData, getToken=False):
        # 登录的url
        url = f'{HOST}/account/sLogin'
        # 调用加密函数，对密码进行加密；字典值修改：字典名[键名]=值
        inData['password'] = Encrypt().get_md5(inData['password'])
        # 请求接口
        resp = requests.post(url, data=inData)
        # print(resp.request.body) # 请求的body
        # print(resp.text)  # 返回是字符串的响应结果
        if getToken:
            return resp.json()['data']['token']  # 返回token
        else:
            return resp.json()  # 前提：响应数据一定要是json才可以使用，返回的是字典

if __name__ == '__main__':
    req = Login().login(login_info, getToken=False)
    print(req)

from PyInterface.config.Config import HOST, login_info, myShop_info
from PyInterface.lib.Login import Login
import requests

# 封装店铺实例；每一次或者每一个店铺的实例，都只需要鉴权一次
class MyShop:
    # 加入token
    def __init__(self, inToken):
        self.header = {'Authorization':inToken}

    # 1，列出店铺
    def shop_list(self, inData):
        # 1,url配置 参数是在url?后面的
        url = f'{HOST}/shopping/myShop'
        # 2,参数
        payload = inData
        # 3,发出请求
        # 4,params
        resp = requests.get(url, params=payload, headers=self.header)
        # return resp.json()  # 返回字典个数
        return resp.text

if __name__ == '__main__':
    # 1,先登录，获取token
    token = Login().login(login_info, getToken=True)
    # 2,店铺列出接口调用
    req = MyShop(token).shop_list(myShop_info)
    print(req)

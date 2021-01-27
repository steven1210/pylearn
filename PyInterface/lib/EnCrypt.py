import hashlib


# 1,封装MD5加密类
class Encrypt:
    # 2,封装加密函数
    def get_md5(self, password):
        # 1,实例化加密对象
        md5 = hashlib.md5()
        # 2，进行加密操作
        md5.update(password.encode('utf-8'))
        # 3，返回加密后的结果
        return md5.hexdigest()


if __name__ == '__main__':
    print(Encrypt.get_md5('14459'))

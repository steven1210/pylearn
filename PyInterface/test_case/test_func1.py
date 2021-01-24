import pytest
import os
import allure


# 封装测试类
@allure.feature('登录功能')
class TestLogin:
    # 该测试类--前置操作--初始化
    def setup_class(self):  # 看业务本身--可选项
        print('执行测试类之前，我需要执行操作----')

    # 定义函数类型 -- 测试用例
    # 数据驱动
    @allure.story('登录模块1')
    @allure.title('相加')
    @pytest.mark.parametrize('a,b', [(1, 2), (3, 4), (5, 6)])
    def test_add(self, a, b):
        print('----test_add----')
        assert a + 1 == b  # 断言

    @allure.story('登录模块2')
    @allure.title('相乘')
    @pytest.mark.parametrize('a', [1, 2, 3])
    def test_pare(self, a):
        print('----test_pare----')
        assert 1 * 1 == a  # 断言

    def teardown_class(self):  # 看业务本身--可选项
        print('---该测试类的环境清除---')


if __name__ == '__main__':
    # 需要打印对应的信息 -s
    # 1,--alluredir 存放目录
    pytest.main(['test_func1.py', '-s', '--alluredir', '../report/tmp'])
    # 2,allure generate allure 报告 cmd指令--os.system()
    # allure generate 报告需要的数据 -o 报告存放的目录 --clean(清除上次报告数据)
    os.system('allure generate ../report/tmp -o ../report/report --clean')

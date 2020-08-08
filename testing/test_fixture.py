import pytest

#创建一个登录的fixture方法，yield关键字激活了fixture的teardown方法
#fixture是pytest的外壳函数，可以模拟setup,teardown操作
#yield之前的操作相当于setup，yield之后的操作相当于teardown
#yield相当于return，如果想要return一些测试数据，可以放在yield后面返回到测试用例中
@pytest.fixture(autouse=True)
def login():
    pass
    print("登录操作")
    print("获取token")
    username="tom"
    password="123456"
    token="token2133fdafafda"
    #return[username,password]
    yield[username,password,token]
    print("登出操作")

#测试用例1：需要提前登录
#在执行测试用例之前会执行传入的fixture方法
def test_case1(connectDB):
    print(f"login,username and password:{login}")
    print("测试用例1")
#测试用例2：不需要提前登录
def test_case2(connectDB):
    print("测试用例2")
#测试用例3：需要提前登录
def test_case3():
    print("测试用例3")
def test_case4():
    print("测试用例4")
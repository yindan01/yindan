import requests
class TestDepartment:
    def setup(self):
        '''
        获取token
        '''
   # 定义凭证
        corpid = "wwf353e31c6d0d3f63"
        corpsecret = "kz2ZTtydcXtnkAYkcEhif3S90heiCea2thyNWq7VQxg"
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        #定义请求参数
        params={
            "corpid": corpid,
            "corpsecret":corpsecret
        }
        #发get请求
        r=requests.get(url=url,params=params)
        #获取token值
        self.token=r.json()["access_token"]
    def test_create_department(self):
        '''
        创建部门
        :return:
        '''
        url="https://qyapi.weixin.qq.com/cgi-bin/department/create"
        #定义请求参数
        param={
            "access_token":self.token
        }
        #定义请求体
        data={
            "name": "技术部",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        #发post请求
        r=requests.post(url=url,json=data,params=param)
        #打印响应数据
        print(r.json())
        #断言
        assert r.json()["errcode"]==0 and r.json()["errmsg"]=="created"
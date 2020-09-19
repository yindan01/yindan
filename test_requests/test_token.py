import requests
class TestToken:
    def test_get_token(self):
        '''
        获取 access_token

        '''
        #定义凭证
        corpid="wwf353e31c6d0d3f63"
        corpsecret="kz2ZTtydcXtnkAYkcEhif6qRZkujpRG1D-cHz7COp_Y"


        url=f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        #发get请求
        r=requests.get(url=url)
        #打印相应数据
        print(r.json())



    def test_token_param(self):
        '''
        获取 token的第二种形式

        '''
        # 定义凭证
        corpid = "wwf353e31c6d0d3f63"
        corpsecret = "kz2ZTtydcXtnkAYkcEhif6qRZkujpRG1D-cHz7COp_Y"
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        #定义请求参数
        params={
            "corpid": corpid,
            "corpsecret":corpsecret
        }
        #发get请求
        r=requests.get(url=url,params=params)
        #打印响应数据
        print(r.json())

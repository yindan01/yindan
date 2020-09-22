import pytest
import requests
class TestToken:
    #前面定义的是参数的名称，后面定义的是参数具体的值，以【{}；{}】
    @pytest.mark.parametrize(
       "corp_id,corp_secret,errmsg",
        [("wwf353e31c6d0d3f63","kz2ZTtydcXtnkAYkcEhif3S90heiCea2thyNWq7VQxg","ok"),
         ("","kz2ZTtydcXtnkAYkcEhif3S90heiCea2thyNWq7VQxg","corpid missing"),
         ("wwf353e31c6d0d3f63","","corpsecret missing")])
    #在定义方法的时候，需要定义出来pytest装饰器中定义的形参
    def test_token(self,corp_id,corp_secret,errmsg):
        # corp_id="wwf353e31c6d0d3f63"
        # corp_secret="kz2ZTtydcXtnkAYkcEhif3S90heiCea2thyNWq7VQxg"
        token_url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r= requests.get(url=token_url)
        print(r.json())
        # #验证corpsecret必填逻辑是否生效
        assert r.json()["errmsg"]==errmsg
        # assert r.json()["errmsg"] == 'corpid missing'
        # #assert r.json()["errcode"]==0


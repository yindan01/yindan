import requests


class Wework():

    def get_token(self):
        '''

        :return:
        '''
        corp_id = "wwf353e31c6d0d3f63"
        corp_secret = "kz2ZTtydcXtnkAYkcEhif4ylVCTk2iQx4qMqYvDOOXs"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        return r.json()["access_token"]
# Author: eckoqzhang
# Date: 2018-11-03
# Desc: Any question Pls contact eckoqzhang@163.com

import sys

from utils.http import CHttp
import conf

class CLogin(object):
    def __init__(self,
                 js_code,
                 appid = conf.AppID, 
                 secret = conf.AppSecret, 
                 grant_type='authorization_code'):

        self._appid = appid
        self._secret = secret
        self._js_code = js_code
        self._grant_type = grant_type
        self._login_url = "https://api.weixin.qq.com/sns/jscode2session"

    def login(self):
        data = {
                "appid" : self._appid,
                "secret": self._secret,
                "js_code": self._js_code,
                "grant_type" : self._grant_type
               }
        login_http = CHttp(self._login_url, data)
        return login_http.http_get()

if __name__ == "__main__":
    obj = CLogin("071guFmE1Vek070gO0nE1Z7CmE1guFmE")
    print obj.login()

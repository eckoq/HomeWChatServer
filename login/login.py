# Author: eckoqzhang
# Date: 2018-11-03
# Desc: Any question Pls contact eckoqzhang@163.com

import sys

from HomeWChat.utils.http import CHttp
from HomeWChat.utils.wx_crypt import CWxCrypt 
from HomeWChat.utils import utils
from HomeWChat import conf
from .models import User
import login_errno

class CLogin(object):
    def __init__(self,
                 js_code,
                 appid = conf.AppID, 
                 secret = conf.AppSecret, 
                 grant_type='authorization_code'):
        self._openid = ""
        self._session_key = ""
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
        retmsg = login_http.http_get()
        if retmsg["errno"] == 0:
            self._openid = retmsg["data"]["openid"]
            self._session_key = retmsg["data"]["session_key"]
            return 0
        return retmsg["errno"]
    
    def get_openid(self):
        return self._openid

    def get_session_key(self):
        return self._session_key
    
    def check_login(self):
        u = User.objects.filter(openid=self._openid).first()
        if u is not None:
            return 0
        return login_errno.LOGIN_USER_NOT_EXIST

    def register(self, iv, encryptedData, referrer):
        errno = self.login()
        if errno != 0:
            return errno

        k = CWxCrypt(self._appid, self._session_key)
        decryed = k.decrypt(encryptedData, iv)

        user_obj = User.objects.create(last_login=utils.now(), username=decryed["nickName"], 
                                       openid=decryed["openId"], city=decryed["city"],     
                                       country=decryed["country"], gender=decryed["gender"],
                                       province=decryed["province"])
        user_obj.save()
        return 0
            
if __name__ == "__main__":
    obj = CLogin("071guFmE1Vek070gO0nE1Z7CmE1guFmE")
    print obj.login()

# Author: eckoqzhang
# Date: 2018-11-03
# Desc: Any question Pls contact eckoqzhang@163.com

class CLogin(obj):
    def __init__(appid, 
                 secret, 
                 js_code='JSCODE',
                 grant_type='authorization_code'):

        self._appid = appid
        self.secret = secret
        self._js_code = js_code
        self._grant_type = grant_type
        self._login_url = "https://api.weixin.qq.com/sns/jscode2session?"
    
   def login()



if __name__ == "__main__":
    print "hello world"

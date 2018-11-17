# Author: eckoqzhang
# Date: 2018-11-17   
# Desc: Any question Pls contact to eckoqzhang@163.com

#-*- coding:utf-8 -*-

import urllib2
import json
import sys

ERR_HTTP_PARAM  = -10000
ERR_HTTP_REQ    = -10001

class CHttp(object):
    def __init__(self, url, data):
        self._url   = url
        self._data  = data
        self._retmsg    = {
                "errno" : 0,
                "errmsg": "request ok"
            }

    def __set_errinfo(self, errno, errmsg):
        self._retmsg["errno"]   = errno
        self._retmsg["errmsg"]  = errmsg
        return self._retmsg

    def http_get(self):
        try:
            if not isinstance(self._data, dict):
                return self.__set_errinfo(ERR_HTTP_PARAM, "data is not dict")
            
            params = "?"
            for key in self._data.keys():
                params += '%s=%s&' %(key, str(self._data[key]))
            params = params.strip('&') 
            
            url     = self._url + params 
            request = urllib2.Request(url)
            request.get_method  = lambda:'GET'
            response    = urllib2.urlopen(request, timeout=600)
            result = json.loads(response.read(), 'latin_1')
            self._retmsg["data"] = result
            return self._retmsg

        except Exception,e:
            return self.__set_errinfo(ERR_HTTP_REQ, "%s" %(e))

    def http_post(self):
        try:
            if not isinstance(self._data, dict):
                return self.__set_errinfo(ERR_HTTP_PARAM, "data is not dict")
            
            params  = json.dumps(self._data)
            request = urllib2.Request(url, params)
            request.get_method  = lambda:'POST'
            response    = urllib2.urlopen(request, timeout=600)
            result  = json.loads(response.read(), 'latin_1')
            self._retmsg["data"]    = result
            return self._retmsg

        except Exception,e:
            return self.__set_errinfo(ERR_HTTP_REQ, "%s" %(e))
        
    
if __name__ == "__main__":
    obj = CHttp("https://api.weixin.qq.com/sns/jscode2session", {"appid":1, "secret":"23", "js_code":"jscode"})
    print obj.http_get()
    pass

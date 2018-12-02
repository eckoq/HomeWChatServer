# Author: eckoqzhang
# Date: 2018-12-02  
# Desc: Any question Pls contact to eckoqzhang@163.com

#-*- coding:utf-8 -*-

import base64
import json
from Crypto.Cipher import AES

class CWxCrypt():
    def __init__(self, appid, session_key):
        self._appid = appid
        self._session_key = session_key

    def decrypt(self, encrypted_data, iv):
        session_key = base64.b64decode(self._session_key)
        encrypted_data = base64.b64decode(encrypted_data)
        iv = base64.b64decode(iv)

        cipher = AES.new(session_key, AES.MODE_CBC, iv)
        decrypted = json.loads(self._unpad(cipher.decrypt(encrypted_data)))

        if decrypted['watermark']['appid'] != self._appid:
            raise Exception('Invalid Buffer')
        
        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


if __name__ == "__main__":

    appId       = 'wx4f4bc4dec97d474b'
    sessionKey  = 'tiihtNczf5v6AKRyjwEUhQ=='
    iv  = 'r7BXXKkLb8qrSNn05n0qiA=='
    encryptedData = 'CiyLU1Aw2KjvrjMdj8YKliAjtP4gsMZMQmRzooG2xrDcvSnxIMXFufNstNGTyaGS9uT5geRa0W4oTOb1WT7fJlAC+oNPdbB+3hVbJSRgv+4lGOETKUQz6OYStslQ142dNCuabNPGBzlooOmB231qMM85d2/fV6ChevvXvQP8Hkue1poOFtnEtpyxVLW1zAo6/1Xx1COxFvrc2d7UL/lmHInNlxuacJXwu0fjpXfz/YqYzBIBzD6WUfTIF9GRHpOn/Hz7saL8xz+W//FRAUid1OksQaQx4CMs8LOddcQhULW4ucetDf96JcR3g0gfRK4PC7E/r7Z6xNrXd2UIeorGj5Ef7b1pJAYB6Y5anaHqZ9J6nKEBvB4DnNLIVWSgARns/8wR2SiRS7MNACwTyrGvt9ts8p12PKFdlqYTopNHR1Vf7XjfhQlVsAJdNiKdYmYVoKlaRv85IfVunYzO0IKXsyl7JCUjCpoG20f0a04COwfneQAGGwd5oa+T8yO5hzuyDb/XcxxmK01EpqOyuxINew=='

    pc = CWxCrypt(appId, sessionKey)

    print json.dumps(pc.decrypt(encryptedData, iv))

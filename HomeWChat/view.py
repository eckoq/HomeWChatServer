# Author: eckoqzhang
# Date: 2018-10-10
# Desc: Any question Pls contact eckoqzhang@163.com

from django.http import HttpResponse

import json

from login import CLogin
 
def hello(request):
    return HttpResponse("Hello world ! ")

def login(request):
    if request.method == "GET":
        code    = request.GET["code"]
    else :
        code    = request.POST["code"]

    obj = CLogin(code)

    data    = json.dumps(obj.login())
    return HttpResponse(data, content_type="application/json")

if __name__ == "__main__":
    print login(0, 1, "23")

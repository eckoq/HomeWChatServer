# Author: eckoqzhang
# Date: 2018-10-10
# Desc: Any question Pls contact eckoqzhang@163.com

# -*- coding: utf-8 -*-
from django.http import HttpResponse

import json

def hello(request):
    return HttpResponse("Hello world ! ")

if __name__ == "__main__":
    pass

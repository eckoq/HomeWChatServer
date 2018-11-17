# Author: eckoqzhang
# Date: 2018-10-10
# Desc: Any question Pls contact eckoqzhang@163.com

from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")

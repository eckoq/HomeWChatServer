# Author: eckoqzhang
# Date: 2018-10-10
# Desc: Any question Pls contact eckoqzhang@163.com

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("hello news");



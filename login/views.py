# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import json
from login import CLogin

def login(request):
    if request.method == "GET":
        code    = request.GET["code"]
    else :
        code    = request.POST["code"]

    obj = CLogin(code)
    data    = json.dumps(obj.login())

    return HttpResponse(data, content_type="application/json")
     

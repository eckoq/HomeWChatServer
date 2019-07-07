# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import json
from login import CLogin

@csrf_exempt
def login(request):
    if request.method == "GET":
        code    = request.GET["code"]
    else :
        code    = request.POST["code"]
    
    data = {
             "errno": 0,
             "msg": ""
            }
    obj = CLogin(code)
    retcode = obj.login()
    if retcode != 0:
        data["errno"] = retcode
        data["msg"] = "login failed"
    
    retcode = obj.check_login()
    if retcode != 0:
        data["errno"] = retcode
        data["msg"] = "login failed"

    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def register(request):
    if request.method == "GET":
        code    = request.GET["code"]
        iv      = request.GET["iv"]
        encryptedData = request.GET["encryptedData"]
        referrer = request.GET["referrer"]
    else :
        code    = request.POST["code"]
        iv      = request.POST["iv"]
        encryptedData = request.POST["encryptedData"]
        referrer = request.POST["referrer"]

    data = {
            "errno": 0,
            "msg":""
            }
    obj = CLogin(code)
    data["msg"] = obj.register(iv, encryptedData, referrer)
    return HttpResponse(json.dumps(data), content_type="application/json")

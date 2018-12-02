from django.shortcuts import render

# Create your views here.


import random
import json
import time
import requests
from main import models

def login(request):
    if request.method == 'POST':
        code = json.loads(request.body.decode())['code']
        res = requests.get("https://api.weixin.qq.com/sns/jscode2session?appid=wx7f8e3abb8c49174e&secret=db01f42467b56c7eec14faa1b1513ba7&js_code={}&grant_type=authorization_code".format(code))
        res_dic = res.json()
        openid = res_dic['res_dic']
        session_key = res_dic['session_key']
        return HttpResponse(res)
    return HttpResponse('get login')


def password(requset):
    obj = models.Password.objects.filter(device_id='wilde007').order_by('used_time').first()
    models.Password.objects.filter(id=obj.id).update(used_time=int(time.time()))
    return HttpResponse(obj.password)


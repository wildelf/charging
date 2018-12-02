from django.shortcuts import render,HttpResponse

# Create your views here.


import json
import time
import requests
from main import models,api

def login(request):
    if request.method == 'POST':
        result = {}
        code = request.POST.get('code')
        name = request.POST.get('name')
        # body = json.loads(request.body.decode())
        # code = body['code']
        # name = body['name']
        res = requests.get("https://api.weixin.qq.com/sns/jscode2session?appid=wx7f8e3abb8c49174e&secret=db01f42467b56c7eec14faa1b1513ba7&js_code={}&grant_type=authorization_code".format(code))
        res_dic = res.json()
        errcode = res_dic['errcode']
        errmsg = res_dic['errmsg']
        if errcode==0:
            openid = res_dic['res_dic']
            session_key = res_dic['session_key']
            token = api.get_random_token()
            obj = models.User(name=name,openid=openid,session_key=session_key,token=token)
            obj.save()
            id = obj.id
            result['status'] = 0
            result['id'] = id
            result['token'] = token
        else:
            result['status'] = -1
            result['errmsg'] = errmsg
        return HttpResponse(json.dumps(result))

    return HttpResponse('404')


def password(requset):
    obj = models.Password.objects.filter(device_id='wilde007').order_by('used_time').first()
    models.Password.objects.filter(id=obj.id).update(used_time=int(time.time()))
    return HttpResponse(obj.password)


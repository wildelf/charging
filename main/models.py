from django.db import models

# Create your models here.



class User(models.Model):
    name = models.CharField(max_length=64,verbose_name='用户名')
    session_key = models.CharField(max_length=64)
    openid = models.CharField(max_length=64)
    token = models.CharField(max_length=64)
    pwd = models.CharField(max_length=64)
    pay_list = models.ForeignKey('PayList',verbose_name='支付列表')

class PayList(models.Model):
    datetime = models.IntegerField()



class Password(models.Model):
    device_id = models.CharField(max_length=64,verbose_name='设备id')
    password = models.CharField(max_length=4,verbose_name='密码')
    used_time = models.IntegerField(verbose_name='使用时间',default=0)
    def __str__(self):
        return self.device_id
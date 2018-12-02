from django.db import models

# Create your models here.

class Password(models.Model):
    device_id = models.CharField(max_length=64,verbose_name='设备id')
    password = models.CharField(max_length=4,verbose_name='密码')
    used_time = models.IntegerField(verbose_name='使用时间',default=0)
    def __str__(self):
        return self.device_id
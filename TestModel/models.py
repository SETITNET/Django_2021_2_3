from django.db import models
import os

# Create your models here.

# Test 表示数据库表名，继承了models.Model
# name 为数据表中的字段，数据类型则由CharField
class Test(models.Model):
    name = models.CharField(max_length=20)

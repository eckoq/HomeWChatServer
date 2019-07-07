# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    openid = models.TextField()
    gender = models.IntegerField(default=0) 
    country = models.TextField(default='unkown')
    province = models.TextField(default='unkown')
    city = models.TextField(default='unkown')


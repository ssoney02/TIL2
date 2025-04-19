from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # 팔로잉 팔로워 기능 구현 -> 다대다 모델
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers'),

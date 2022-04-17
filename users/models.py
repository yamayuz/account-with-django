from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Meta:
        db_table = 'custom_user'

    login_count = models.IntegerField(verbose_name='ログイン回数', default=0)
    profile_image = models.ImageField(verbose_name='プロフィール画像', null=True, blank=True)




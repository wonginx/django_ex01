from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,
                                related_name = 'profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)
    # DB 에 마이그레이션 적용하기 > pip install pillow > makemigration(변화추적) / migrate(실제변화적용)
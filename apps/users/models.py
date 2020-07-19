from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username

    def get_profile_avatar(self):
        default_avatar = settings.STATIC_URL + 'img/default.png'
        if self.avatar:
            return self.avatar.url
        else:
            return default_avatar

# Create your models here.

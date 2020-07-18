from django.conf import settings
from django.db import models
from django.utils import timezone


def logo_upload_to(instance, filename):
    return 'subsites/%s/logo/%s' % (instance.subsite_slug, filename)


class Subsite(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='subsites',
        verbose_name='Автор',
        null=True,
    )
    subsite_name = models.CharField(max_length=50, null=True, verbose_name='Имя сайта')
    subsite_slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    subsite_logo = models.ImageField(upload_to=logo_upload_to, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'
        ordering = ('-created_at',)

    def __str__(self):
        return self.subsite_name

# Create your models here.

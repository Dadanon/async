from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from .utils import get_reading_time
from slugify import slugify
from subsites.models import Subsite


class ArticleQuerySet(models.query.QuerySet):
    def get_published(self):
        return self.filter(status='P')

    def get_draft(self):
        return self.filter(status='D')

    def get_for_day(self):
        qs = self.get_published()
        last_day = timezone.now() - timezone.timedelta(days=1)
        qs = qs.filter(created_at__gt=last_day)
        return qs

    def get_for_week(self):
        qs = self.get_published()
        last_week = timezone.now() - timezone.timedelta(days=7)
        qs = qs.filter(created_at__gt=last_week)
        return qs

    def get_for_all(self):
        qs = self.get_published()
        return qs

    def get_by_user(self, author):
        qs = self.get_published()
        if author:
            qs = qs.filter(author=author)
            return qs



class Article(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS = (
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликовано'),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='articles',
        null=True,
    )
    subsite = models.ForeignKey(
        Subsite,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posted_subsites',
        verbose_name='Подсайт',
    )
    title = models.CharField(max_length=120, verbose_name='Заголовок', help_text='Максимально - 120 символов')
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True, editable=True)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS, default=DRAFT)
    created_at = models.DateTimeField(default=timezone.now)
    reading_time = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ArticleQuerySet.as_manager()
    slug_field_name = 'slug'
    slug_from = 'title'

    class Meta():
        verbose_name = 'статью'
        verbose_name_plural = 'статьи'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.author.username}-{self.title}', lowercase=True)
        self.reading_time = get_reading_time(self.body)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

# Create your models here.

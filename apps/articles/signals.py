"""from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Article
import slugify.slugify


@receiver(post_save, sender=Article)
def create_slug(sender, instance, signal, *args, **kwargs):
    if instance.id and hasattr(instance, 'slug_field_name') and hasattr(instance, 'slug_from'):
        slug_name = instance.slug_field_name
        slug_from = instance.slug_from
        if not getattr(instance, slug_name, None):
            slug = '%s-' % instance.id + slugify.slugify(getattr(instance, slug_from), lowercase=True)
            setattr(instance, slug_name, slug)
            instance.save()"""

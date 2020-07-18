from django.contrib import admin
from .models import Subsite

@admin.register(Subsite)


class SubsiteAdmin(admin.ModelAdmin):
    pass

# Register your models here.

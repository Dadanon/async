from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', include('users.urls')),  # new
    path('users/', include('django.contrib.auth.urls')),  # new
    path('', include('articles.urls')),
    path('', include('subsites.urls')),
]

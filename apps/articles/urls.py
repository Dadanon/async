from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_for_all, name='all_news'),
    path('daily', views.article_for_day, name='daily_news'),
    path('weekly', views.article_for_week, name='weekly_news'),
    path('<subsite>/<slug>', views.ArticleDetailView.as_view(), name='detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('<username>', views.UserProfileView.as_view(), name='user_profile'),
]
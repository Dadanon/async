from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import CustomUser
from articles.models import Article


class UserDetailView(DetailView):
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        object = super().get_object()
        context['own_profile'] = True if self.request.user == object else False
        return context


class UserProfileView(UserDetailView):
    template_name = 'users/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        object = super().get_object()
        context['submitted_articles'] = Article.objects.get_by_user(author=object)
        return context

# Create your views here.

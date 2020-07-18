from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class MyUserCreationForm(UserCreationForm):
    error_messages = UserCreationForm.error_messages.update({
        'duplicate_username': 'Это имя пользователя уже занято',
    })

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])



@admin.register(CustomUser)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username', 'age', )
    search_fields = ('id', 'age', 'email', )

# Register your models here.

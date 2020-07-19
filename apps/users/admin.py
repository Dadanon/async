from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
    UserCreationForm.error_messages['duplicate_username'] = 'Это имя пользователя уже занято'
    error_messages = UserCreationForm.error_messages

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
    fieldsets = AuthUserAdmin.fieldsets + (
        ('Данные пользователя', {
            'fields': ('avatar', )
        }),
    )
    list_display = ('username', 'age')
    search_fields = ['id', 'age', 'email']




# Register your models here.

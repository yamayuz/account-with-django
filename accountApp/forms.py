from django import forms
from users.models import CustomUser

class SignupForm(forms.Form):
    username = forms.CharField(label='ユーザ名', max_length=150)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            CustomUser.objects.get(username=username)
            raise forms.ValidationError('このユーザは登録済みです。')
        except CustomUser.DoesNotExist:
            return username

    
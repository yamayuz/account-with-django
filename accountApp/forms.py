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

    
class SigninForm(forms.Form):
    username = forms.CharField(label='ユーザ名', max_length=150)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError('登録されていないユーザーです。\nユーザーを登録してください。')

        if not user.check_password(password):
            raise forms.ValidationError('正しいパスワードを入力してください。')


    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     try:
    #         CustomUser.objects.get(username=username)
    #         return username
    #     except CustomUser.DoesNotExist:
    #         raise forms.ValidationError('登録されていないユーザーです。\nユーザーを登録してください。')
            

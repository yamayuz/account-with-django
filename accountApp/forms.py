from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='ユーザ名', max_length=150)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if username == '':
    #         raise forms.ValidationError('ユーザ名を入力してください')
    #     return username
    
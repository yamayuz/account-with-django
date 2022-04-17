from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User


class UserHomeView(View):
    def get(self, request):
        return render(request, 'user-home.html')


class SigninView(View):
    def get(self, request):
        return render(request, 'signin.html')


class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        target_username = request.POST['username']
        target_password = request.POST['password']
        try:
            User.objects.get(username=target_username)
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています。'})
        except User.DoesNotExist:
            user = User.objects.create_user(target_username, '', target_password)
            return redirect('signin')
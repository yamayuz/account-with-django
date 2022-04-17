from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class UserHomeView(View):
    def get(self, request):
        return render(request, 'user-home.html')


class SigninView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        target_username = request.POST['username']
        target_password = request.POST['password']
        user = authenticate(username=target_username, password=target_password)
        if user is None:
            return render(request, 'signin.html', {'error': '登録されていないユーザーです。\nユーザーを新規作成してください。'})
        else:
            login(request, user)
            return redirect('user-home')
            

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
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import *
from django.template.response import TemplateResponse


@method_decorator(login_required, name='dispatch')
class UserHomeView(View):
    def get(self, request):
        return render(request, 'user-home.html')


class SigninView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        form = SigninForm(request.POST)
        is_valid = form.is_valid()
        if not is_valid:
            return TemplateResponse(request, 'signin.html', {'form': form})

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)

        if request.user.is_superuser or request.user.is_staff:
            return render(request, 'dashboard.html')
        else:
            return redirect('user-home')


class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        form = SignupForm(request.POST)
        is_valid = form.is_valid()
        if not is_valid:
            return TemplateResponse(request, 'signup.html', {'form': form})
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        CustomUser.objects.create_user(username, '', password)
        return redirect('signin')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'logout.html')

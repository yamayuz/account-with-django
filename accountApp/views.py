from django.shortcuts import render
from django.views.generic import View


class UserHomeView(View):
    def get(self, request):
        return render(request, 'user-home.html')
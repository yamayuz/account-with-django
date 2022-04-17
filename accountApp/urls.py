from django.urls import path
from .views import UserHomeView, SigninView

urlpatterns = [
    path('', UserHomeView.as_view(), name='user-home'),
    path('signin', SigninView.as_view(), name='signin'),
]
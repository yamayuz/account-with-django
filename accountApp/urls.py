from django.urls import path
from .views import UserHomeView, SigninView, SignupView

urlpatterns = [
    path('', UserHomeView.as_view(), name='user-home'),
    path('signin', SigninView.as_view(), name='signin'),
    # path('accounts/login', SigninView.as_view(), name='login'),
    path('signup', SignupView.as_view(), name='signup'),
]
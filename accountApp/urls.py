from django.urls import path
from .views import UserHomeView

urlpatterns = [
    path('', UserHomeView.as_view(), name='user-home'),
]
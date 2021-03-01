from django.urls import path
from django.views.generic import TemplateView
from login.views import LoginHome

urlpatterns = [
    path('', LoginHome.as_view(), name='login'),
    path('login/', LoginHome.as_view(), name='login'),
]
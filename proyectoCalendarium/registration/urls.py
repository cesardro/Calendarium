from django.urls import path
from . import views
from .views import RegistroView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.vistasignup,name='vistasignup'),
    path('signup2',RegistroView.as_view(),name='RegistroView'),
    path('login',views.login,name='login'),
    path('password_reset_', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
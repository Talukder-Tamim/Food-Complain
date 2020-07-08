from django.urls import path
from .import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register', views.registerView, name="register"),
    path('login', views.loginView, name="login")
    ]
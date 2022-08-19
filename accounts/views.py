from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse


class SEC_LoginView(LoginView):
    template_name = 'accounts/login.html'



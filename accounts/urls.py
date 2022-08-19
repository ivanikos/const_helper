from django.contrib.auth import views
from django.urls import path
from .views import SEC_LoginView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', SEC_LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout")
]
from django.urls import path
from . import views

app_name = 'weldlog'

urlpatterns = [
    path('', views.index, name='index'),
]
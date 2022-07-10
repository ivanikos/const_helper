from django.urls import path
from . import views

app_name = 'newapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('wlog', views.wl, name='wl'),
    path('mtr', views.mtr, name='mtr'),
    path('nk', views.nk, name='nk'),
    path('create_joint', views.create_joint, name='create'),
    path('summary', views.summary, name='summary'),
    path('autocomplete', views.autocomplete, name='autocomplete'),
    path('autocomplete_line', views.autocomplete_line, name='autocomplete_line'),
    path('splitting_req', views.splitting_requests, name='splitting_request'),
    path('filling_table', views.autofilling_table, name='filling_table')

]
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import *

from account import views


urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'),
    
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),    
    url(r'^logout/$', logout, name='logout'),
)
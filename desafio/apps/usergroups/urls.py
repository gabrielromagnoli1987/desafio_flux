# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from usergroups import views


urlpatterns = patterns('',
    url(r'^$', views.usergroups, name='usergroups'),    
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/(?P<usergroup_id>\d+)/$', views.delete, name='delete'),
    url(r'^edit/(?P<usergroup_id>\d+)/$', views.edit, name='edit'),
)
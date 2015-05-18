# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from documents import views


urlpatterns = patterns('',
    url(r'^$', views.documents, name='documents'),
    # ejemplo: /documents/5/
    url(r'^(?P<document_id>\d+)/$', views.detail, name='detail'),    
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<document_id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<document_id>\d+)/$', views.delete, name='delete'),
)
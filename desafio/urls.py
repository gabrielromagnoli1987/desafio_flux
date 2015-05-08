# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
        
    url(r'^', include('home.urls', namespace="home")),
    url(r'^documents/', include('documents.urls', namespace="documents")),
    url(r'^account/', include('account.urls', namespace="account")),
)


# https://docs.djangoproject.com/en/1.8/howto/static-files/
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
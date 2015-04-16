from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include('home.urls', namespace="home")),
    url(r'^documents/', include('documents.urls', namespace="documents")),
)

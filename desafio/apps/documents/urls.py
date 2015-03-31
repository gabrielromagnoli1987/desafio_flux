from django.conf.urls import patterns, url

from documents import views
from models import Document

urlpatterns = patterns('',
    url(r'^$', views.documents, name='documents'),
    # ex: /documents/5/
    url(r'^(?P<document_id>\d+)/$', views.detail, name='document_detail'),
)
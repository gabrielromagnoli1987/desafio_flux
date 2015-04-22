from django.conf.urls import patterns, url

from documents import views
from models import Document

urlpatterns = patterns('',
    url(r'^$', views.documents, name='documents'),
    # ejemplo: /documents/5/
    url(r'^(?P<document_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
)
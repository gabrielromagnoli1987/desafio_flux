# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


from usergroups.models import UserGroup



class Document(models.Model):
    
    TYPES = (
        ('publico', 'publico'),
        ('privado', 'privado'),
        ('draft', 'draft'),
    )
    
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=7, choices=TYPES)
    date = models.DateTimeField()
    owner = models.ForeignKey(User)
    user_group = models.ForeignKey(UserGroup, blank=True, null=True)
    file = models.FileField()
    
    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now
    
    class Meta():
        
        app_label = 'documents'
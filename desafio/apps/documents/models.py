from django.db import models
from django.contrib.auth.models import User


from usergroups.models import UserGroup

# Create your models here.


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
    user_group = models.ForeignKey(UserGroup)
    path = models.URLField()
    
    def __str__(self):
        return self.name
    
    class Meta():
        
        app_label = 'documents'
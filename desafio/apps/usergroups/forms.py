from django.forms import ModelForm

from usergroups.models import UserGroup


class UserGroupForm(ModelForm):
    
    class Meta:
        model = UserGroup
        fields = ['name', 'description']
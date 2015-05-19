# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from usergroups.models import UserGroup
from usergroups.forms import UserGroupForm


@user_passes_test(lambda u:u.is_staff, login_url=settings.LOGIN_URL)
def usergroups(request):
    usergroups = UserGroup.objects.all()    
    return render(request, "usergroups/usergroups.html", {'usergroups': usergroups})


@user_passes_test(lambda u:u.is_staff, login_url=settings.LOGIN_URL)
def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserGroupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():            
            # process the data in form.cleaned_data as required
            usergroup = form.save()                        
            messages.success(request, 'Saved.')
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('usergroups:usergroups'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserGroupForm()

    return render(request, 'usergroups/add.html', {'form': form})


@user_passes_test(lambda u:u.is_staff, login_url=settings.LOGIN_URL)
def delete(request, usergroup_id):
    usergroup = get_object_or_404(UserGroup, pk=usergroup_id).delete()
    messages.success(request, 'Successfully deleted.')
    return HttpResponseRedirect(reverse('usergroups:usergroups'))


@user_passes_test(lambda u:u.is_staff, login_url=settings.LOGIN_URL)
def edit(request, usergroup_id):
    usergroup = get_object_or_404(UserGroup, pk=usergroup_id)
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserGroupForm(request.POST, instance=usergroup)
        # check whether it's valid:
        if form.is_valid():            
            # process the data in form.cleaned_data as required
            usergroup = form.save()
            messages.success(request, 'Saved.')
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('usergroups:usergroups'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserGroupForm(instance=usergroup)
        return render(request, 'usergroups/edit.html', {'form': form})
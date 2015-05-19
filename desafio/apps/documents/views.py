# -*- coding: utf-8 -*-
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from documents.forms import DocumentForm
from documents.models import Document


def documents(request):
    documents = Document.objects.all()
    return render(request, "documents/documents.html", {'documents': documents})


def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    users = None
    if document.user_group:
        users = document.user_group.user_set.all()    
    return render(request, "documents/detail.html", {'document': document, 'users': users})


@login_required()
def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DocumentForm(request.POST, request.FILES)        
        # check whether it's valid:
        if form.is_valid():            
            # process the data in form.cleaned_data as required
            document = form.save(commit=False)
            document.date = datetime.datetime.now()
            document.save()
            form.save_m2m()
            messages.success(request, 'Saved.')
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('documents:documents'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DocumentForm()

    return render(request, 'documents/add.html', {'form': form})


@login_required()
def delete(request, document_id):
    document = get_object_or_404(Document, pk=document_id)    
    if document.owner == request.user:
        document.delete()
        messages.success(request, 'Successfully deleted.')
    return HttpResponseRedirect(reverse('documents:documents'))


@login_required()
def edit(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DocumentForm(request.POST, instance=document)
        # check whether it's valid:
        if form.is_valid():            
            # process the data in form.cleaned_data as required
            document = form.save()
            messages.success(request, 'Saved.')
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('documents:documents'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DocumentForm(instance=document)
        return render(request, 'documents/edit.html', {'form': form})
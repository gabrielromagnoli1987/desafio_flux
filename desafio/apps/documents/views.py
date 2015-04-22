from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from documents.forms import DocumentForm
from documents.models import Document


# Create your views here.

def documents(request):
    documents = Document.objects.all()    
    return render(request, "documents/documents.html", {'documents': documents})


def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, "documents/detail.html", {'document': document})


def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DocumentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('documents'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DocumentForm()

    return render(request, 'documents/add.html', {'form': form})
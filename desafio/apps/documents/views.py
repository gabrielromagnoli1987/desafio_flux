from django.shortcuts import render

from documents.models import Document 

# Create your views here.

def documents(request):
    documents = Document.objects.all()    
    return render(request, "documents/documents.html", {'documents': documents})

def detail(request, document_id):
    pass
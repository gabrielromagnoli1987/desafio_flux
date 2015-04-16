from django.shortcuts import get_object_or_404, render

from documents.models import Document 

# Create your views here.

def documents(request):
    documents = Document.objects.all()    
    return render(request, "documents/documents.html", {'documents': documents})

def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, "documents/detail.html", {'document': document})
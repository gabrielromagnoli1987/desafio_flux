from django.forms import ModelForm

from documents.models import Document


class DocumentForm(ModelForm):
    class Meta:
        model = Document
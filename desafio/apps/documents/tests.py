import datetime

from django.test import TestCase
from django.utils import timezone

from models import Document


class DocumentMethodTests(TestCase):
    
    def test_document_date(self):
        """
        was_published_recently() should return False for documents whose
        date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_document = Document(date=time)
        self.assertEqual(future_document.was_published_recently(), False)
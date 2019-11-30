from django.test import TestCase, Client
from django.urls import reverse
# from mgr_accounts.models import


class TestViews(TestCase):
    def test_Index_View_GET(self):
        client = Client()
        response = client.get(reverse('accounts:Home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')
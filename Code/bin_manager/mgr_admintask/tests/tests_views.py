from django.test import TestCase, Client
from django.urls import reverse
from mgr_database.models import RequestDetail


class TestViews(TestCase):
    def test_Admin_Index_View_GET(self):
        client = Client()
        response = client.get(reverse('admintask:Admin_Home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'base_admin.html')

    def test_RequestListView_GET(self):
        client = Client()
        response = client.get(reverse('admintask:demand'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'demand.html')
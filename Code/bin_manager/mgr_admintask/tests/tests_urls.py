from django.test import SimpleTestCase
from django.urls import reverse,resolve
from mgr_admintask.views import  AdminIndex,RequestListView


class TestUrls(SimpleTestCase):
    def test_admin_home_url_resolves(self):
        url = reverse('admintask:Admin_Home')
        self.assertEquals(resolve(url).func.__name__ , AdminIndex.__name__)

    def test_home_url_resolves(self):
        url = reverse('admintask:demand')
        self.assertEquals(resolve(url).func.__name__ , RequestListView.__name__)
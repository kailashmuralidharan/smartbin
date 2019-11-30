from django.test import SimpleTestCase
from django.urls import reverse,resolve
from mgr_accounts.views import Index


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('accounts:Home')
        # print (resolve(url).url_name)
        # print (resolve(url).route)
        # print (resolve(url).view_name)
        # print (resolve(url).app_name)
        # print (resolve(url).args)
        # print (resolve(url).kwargs)
        # print (str(resolve(url).func.__name__))
        # print(Index)
        # print (resolve(url))
        self.assertEquals(resolve(url).func.__name__ , Index.__name__)
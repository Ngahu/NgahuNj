from django.test import SimpleTestCase
from django.urls import reverse
# from main_app.views import HomeView


class HomePageTests(SimpleTestCase):
    def test_view_url_by_name(self):
        response = self.client.get(reverse('main_app:home_page'))
        self.assertEquals(response.status_code, 200)

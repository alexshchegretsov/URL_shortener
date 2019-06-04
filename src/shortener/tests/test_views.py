from django.test import TestCase, Client
from django.urls import reverse
from shortener.models import Url
from shortener.views import url_form_handler


class TestView(TestCase):

    def setUp(self):
        self.c = Client()

    def test_url_form_handler_exists_at_desired_location(self):
        response = self.c.get("/")
        self.assertEquals(response.status_code, 200)

    def test_url_form_handler_accessible_by_name(self):
        response = self.c.get(reverse(url_form_handler))
        self.assertEquals(response.status_code, 200)

    def test_url_form_handler_uses_correct_template(self):
        response = self.c.get(reverse(url_form_handler))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortener/home_page.html')

    def test_url_form_handler_POST_method(self):
        response = self.c.post('/',{'long_url': 'http://test.google.com'})
        print(response)

    def test_redirect_to_long_url_GET(self):
        response_1 = self.c.get('/1')
        response_2 = self.c.get('/a')
        self.assertEquals(response_1.status_code, 301)
        self.assertEquals(response_2.status_code, 301)

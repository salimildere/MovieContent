from django.test import TestCase, override_settings
from django.urls import resolve, reverse


class TestContentURLAPIViews(TestCase):
    """
        run:
        python manage.py test movpro.contents.tests.test_urls.TestContentURLAPIViews --keepdb

    """

    def test_content_basic_urls(self):

        url_name_map = (
            ("/api/v1/content/", "contents:content"),
            ("/api/v1/content/create_mock/", "contents:create-mock-content"),
        )

        for url, name in url_name_map:
            self.assertEqual(reverse(name), url)
            self.assertEqual(resolve(url).view_name, name)

    def test_content_urls_with_parameters(self):
        url_name_map = (
            ("/api/v1/content/", "contents:content-detail", "pk"),
        )
        for url, name, param in url_name_map:
            kwargs = {param: "123"}
            url = url + kwargs[param] + "/"
            self.assertEqual(reverse(name, kwargs=kwargs), url)
            self.assertEqual(resolve(url).view_name, name)

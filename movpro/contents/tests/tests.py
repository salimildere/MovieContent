from django.urls import reverse
from rest_framework.test import APITestCase

from movpro.contents.models import Content
from movpro.contents.tests.factories import ContentFactory


class ContentViewSetTestCase(APITestCase):
    def setUp(self):
        ContentFactory.create_batch(10)

    def test_list(self):
        response = self.client.get(reverse("contents:content"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 10)
        self.assertEqual(response.data["count"], 10)
        self.assertIsInstance(response.data, dict)


class ContentDetailViewSetTestCase(APITestCase):
    def setUp(self):
        self.content = ContentFactory()

    def test_detail(self):
        url = reverse("contents:content-detail", kwargs={"pk": f"{self.content.id}"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.content.id)
        self.assertEqual(response.data["title"], self.content.title)
        self.assertEqual(response.data["content_rating"], self.content.content_rating.__str__())

    def test_detail_not_found(self):
        response = self.client.get(reverse("contents:content-detail", kwargs={"pk": 100}))
        self.assertEqual(response.status_code, 404)

    def test_update(self):
        response = self.client.patch(reverse("contents:content-detail", kwargs={"pk": self.content.id}),
                                   {"title": "Updated Title"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_update_not_found(self):
        response = self.client.patch(reverse("contents:content-detail", kwargs={"pk": 100}), {"title": "Updated Title"})
        self.assertEqual(response.status_code, 404)

    def test_delete(self):
        response = self.client.delete(reverse("contents:content-detail", kwargs={"pk": self.content.id}))
        self.assertEqual(response.status_code, 204)

    def test_delete_not_found(self):
        response = self.client.delete(reverse("contents:content-detail", kwargs={"pk": 100}))
        self.assertEqual(response.status_code, 404)


class ContentCreateMockViewSetTestCase(APITestCase):
    def test_create(self):
        response = self.client.post(reverse("contents:create-mock-content"), {"title": "New Title"})
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.data["title"], "New Title")
        self.assertEqual(response.data["id"], Content.objects.first().id)

    def test_create_with_empty_data(self):
        response = self.client.post(reverse("contents:create-mock-content"), {})
        self.assertEqual(response.status_code, 201)
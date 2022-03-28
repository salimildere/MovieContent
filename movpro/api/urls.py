from django.urls import path
from movpro.contents.views import ContentViewSet

urlpatterns = [
    # API
    path("v1/content/", ContentViewSet.as_view(), name="catalogs"),
]

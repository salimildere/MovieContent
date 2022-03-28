from django.urls import path
from movpro.contents.views import ContentViewSet, ContentDetailViewSet

urlpatterns = [
    path("/", ContentViewSet.as_view(), name="content"),
    path("/<int:pk>", ContentDetailViewSet.as_view(), name="content_detail"),
]

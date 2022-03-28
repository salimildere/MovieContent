from django.conf import settings
from django.urls import path
from movpro.contents.views import (
    ContentViewSet,
    ContentDetailViewSet,
    ContentCreateMockViewSet,
)

urlpatterns = [
    path("", ContentViewSet.as_view(), name="content"),
    path("<int:pk>/", ContentDetailViewSet.as_view(), name="content_detail"),
]
if settings.IS_ACTIVE_FACTORY:
    urlpatterns += [
        path(
            "create_mock/",
            ContentCreateMockViewSet.as_view(),
            name="create_mock_content",
        ),
    ]

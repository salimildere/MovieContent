from django.urls import path, include

urlpatterns = [
    # API
    path("v1/content/", include("movpro.contents.urls")),
]

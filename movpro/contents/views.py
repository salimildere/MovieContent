from django.shortcuts import render
from rest_framework import generics

from movpro.contents.models import Content
from movpro.contents.serializers import ContentSerializer


class ContentViewSet(generics.ListAPIView):
    """
    A viewset for listing and retrieving content.
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

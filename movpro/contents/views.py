from django.shortcuts import render
from rest_framework import generics

from movpro.contents.models import Content
from movpro.contents.serializers import ContentSerializer, ContentDetailSerializer


class ContentViewSet(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentDetailSerializer

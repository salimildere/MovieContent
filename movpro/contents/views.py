from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from movpro.contents.models import Content
from movpro.contents.serializers import ContentSerializer, ContentDetailSerializer
from movpro.contents.tests.factories import ContentFactory


class ContentViewSet(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, *args, **kwargs):
        return super(ContentViewSet, self).get(request, *args, **kwargs)


class ContentDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentDetailSerializer


class ContentCreateMockViewSet(GenericAPIView):
    serializer_class = ContentDetailSerializer

    def post(self, *args, **kwargs):
        content = ContentFactory()
        serializer = ContentDetailSerializer(content)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

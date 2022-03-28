from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from movpro.contents.models import Content
from movpro.contents.serializers import ContentSerializer, ContentDetailSerializer
from movpro.contents.tests.factories import ContentFactory


class ContentViewSet(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentDetailSerializer


class ContentCreateMockViewSet(GenericAPIView):
    serializer_class = ContentDetailSerializer

    def post(self, *args, **kwargs):
        content = ContentFactory()
        serializer = ContentDetailSerializer(content)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

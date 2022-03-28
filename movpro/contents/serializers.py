from rest_framework import serializers

from movpro.contents.models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'title', 'imdb_rating', 'made_year', 'image', 'director', 'genre', 'content_rating')


class ContentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

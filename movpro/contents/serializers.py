from rest_framework import serializers

from movpro.contents.models import Content


class ContentBaseSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    genre = serializers.StringRelatedField(many=True)
    content_rating = serializers.StringRelatedField()

    class Meta:
        model = Content
        fields = "__all__"


class ContentSerializer(ContentBaseSerializer):
    class Meta:
        model = Content
        fields = (
            "id",
            "title",
            "imdb_rating",
            "made_year",
            "image",
            "director",
            "genre",
            "content_rating",
        )


class ContentDetailSerializer(ContentBaseSerializer):
    actress = serializers.StringRelatedField(many=True)

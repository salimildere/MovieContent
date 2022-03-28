from rest_framework import serializers

from movpro.contents.models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"
        # fields = ('id', 'name', 'description', 'file', 'created_at', 'updated_at')
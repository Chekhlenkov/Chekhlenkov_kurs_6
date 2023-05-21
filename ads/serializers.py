from rest_framework import serializers

from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    ad = serializers.SlugRelatedField(read_only=True, slug_field="title")
    author = serializers.SlugRelatedField(read_only=True, slug_field="first_name", )

    class Meta:
        model = Comment
        fields = ['id', 'ad', 'author', 'text', 'created_at', ]


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="first_name", )
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ["id", "author", "title", "price", "description", "image", "created_at", "comments", ]

    def get_comments(self, obj):
        return [CommentSerializer(com).data for com in obj.comments_by_ad.all()]


from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Author
        fields = ['id', 'author']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    p_author = AuthorSerializer(
        required=True,
    )
    category = CategorySerializer(
        many=True,
    )

    class Meta:
        model = Post
        fields = ['id', 'p_author', 'genre', 'time_in', 'category', 'title', 'main_text', 'p_rating']

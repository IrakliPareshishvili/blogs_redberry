from rest_framework import serializers
from .models import Category, Blog


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'text_color', 'background_color']

   

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'image', 'publish_date', 'categories', 'author']

    

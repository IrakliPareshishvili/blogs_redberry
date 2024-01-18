from rest_framework import serializers
from .models import Category, Blog

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Blog
        fields = '__all__'

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
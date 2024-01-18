from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'publish_date': ['exact'],
        'categories': ['exact'],
    }

# class ObtainTokenView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         # Your token creation logic here
#         token, created = Token.objects.get_or_create(user=request.user)
#         return Response({'token': token.key})

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': "invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        


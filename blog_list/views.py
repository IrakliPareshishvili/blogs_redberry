from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
# from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer, LoginSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})


class BlogListCreateView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'categories': ['exact']}

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})


class BlogRetrieveView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        user = authenticate(request, email=email)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)




# from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate, login
# from rest_framework import viewsets
# from rest_framework import status
# from rest_framework.response import Response
# from .models import Category, Blog
# from .serializers import CategorySerializer, BlogSerializer, LoginSerializer
# from rest_framework import permissions
# from django_filters.rest_framework import DjangoFilterBackend



# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     # permission_classes = [permissions.IsAuthenticated]

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'data': serializer.data})

# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = {
#         'categories': ['exact'],
#     }

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'data': serializer.data})






# class LoginAPIView(APIView):
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data['email']

#         user = authenticate(request, email=email)

#         if user:
#             login(request, user)
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else:
#             return Response({'error': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


        



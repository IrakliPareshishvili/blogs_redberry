from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import LoginAPIView, BlogListCreateView, BlogRetrieveView, CategoryListView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# BlogViewSet, CategoryViewSet,

# router = DefaultRouter()
# router.register(r'blogs', BlogViewSet, basename='blog')
# router.register(r'categories', CategoryViewSet, basename='category')

schema_view = get_schema_view(
    openapi.Info(
        title="Added Blog List API",
        default_version='v1',
        description="API for managing blogs and categories. This API allows you to perform CRUD operations on blogs and categories. Explore the documentation to understand the available endpoints and their functionalities.",
        
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    
)

urlpatterns = [
    # path('', include(router.urls)),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogRetrieveView.as_view(), name='blog-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

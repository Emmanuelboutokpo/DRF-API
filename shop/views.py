from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from shop.models import Category,Product,Article
from shop.serializers import CategoryListSerializer, CategoryDetailSerializer, ProductListSerializer, ProductDetailSerializer ,ArticleSerializer

class MultipleSerializerMixin:
    detail_serializer_class = None
    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

class CategoryViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
 
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
 
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()
    
class ProductViewset(ReadOnlyModelViewSet):
 
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer
 
    def get_queryset(self):
        return Product.objects.filter(active=True)
 
    def get_serializer_class(self):

        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

class ArticleViewset(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer
 
    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset
    

# for the admin
class AdminCategoryViewset(MultipleSerializerMixin, ModelViewSet):
 
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer
 
    def get_queryset(self):
        return Category.objects.all()
from rest_framework import serializers
 
from shop.models import Product, Category,Article

# for admin
class CategoryListSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'description']
 
    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError('Category already exists')
        return value
 
    def validate(self, data):
        if data['name'] not in data['description']:
            raise serializers.ValidationError('Name must be in description')
        return data
    
# for users
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =  ['id', 'date_created', 'date_updated', 'name']


class ProductDetailSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields =  ['id', 'date_created', 'date_updated', 'name', 'category', 'articles']

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data

class CategoryDetailSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductDetailSerializer(queryset, many=True)
        return serializer.data
    
class ArticleSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Article
        fields =  ['id', 'date_created', 'date_updated', 'name', 'price', 'product']

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
 
from shop.views import CategoryViewset,ProductViewset,ArticleViewset, AdminCategoryViewset

router = routers.SimpleRouter()

#user endpoint
router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

#admin endpoint
router.register('admin/category', AdminCategoryViewset, basename='admin-category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))  # Il faut bien penser à ajouter les urls du router dans la liste des urls disponibles.
]
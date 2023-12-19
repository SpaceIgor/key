from django.urls import path

from .views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    ChangeParentCategoryAPIView,
    CategoriesContainingProductsView,
    ProductsInCategoryView,
    ProductCountInCategoriesView,
    UniqueProductCountInCategoriesView,
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
    path('categories/<int:pk>/change-parent/', ChangeParentCategoryAPIView.as_view(), name='change-parent-category'),
    path('categories-containing-products/', CategoriesContainingProductsView.as_view(),
         name='categories-containing-products'),
    path('categories/<int:category_id>/products/', ProductsInCategoryView.as_view(), name='products-in-category'),
    path('categories/product-count/', ProductCountInCategoriesView.as_view(), name='product-count-in-categories'),
    path('categories/unique-product-count/', UniqueProductCountInCategoriesView.as_view(),
         name='unique-product-count-in-categories'),

]

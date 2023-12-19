from django.db.models import Count
from rest_framework import generics
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, ChangeParentCategorySerializer, \
    CategoriesContainingProductSerializer, ProductCountInCategoriesSerializer, UniqueProductCountInCategoriesSerializer


# a
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# b
class ChangeParentCategoryAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = ChangeParentCategorySerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        new_parent_id = serializer.validated_data['new_parent_id']

        try:
            new_parent = Category.objects.get(pk=new_parent_id)
        except Category.DoesNotExist:
            return Response({'error': 'Нова батьківська категорія не існує'}, status=status.HTTP_400_BAD_REQUEST)

        instance.parent = new_parent
        instance.save()

        return Response({'success': 'Батьківська категорія змінена успішно'}, status=status.HTTP_200_OK)


# c
class CategoriesContainingProductsView(generics.ListAPIView):
    serializer_class = CategoriesContainingProductSerializer

    def get_queryset(self):
        product_ids = self.request.query_params.getlist('product_ids', [])

        categories = Product.objects.filter(id__in=product_ids).distinct()

        return categories

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# d
class ProductsInCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')

        category = Category.objects.get(pk=category_id)
        descendant_categories = category.get_descendants(include_self=True)

        products = Product.objects.filter(categories__in=descendant_categories).distinct()

        return products

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# e
class ProductCountInCategoriesView(generics.ListAPIView):
    serializer_class = ProductCountInCategoriesSerializer

    def get_queryset(self):
        category_ids = self.request.query_params.getlist('category_ids', [])

        queryset = Category.objects.filter(id__in=category_ids).values('id', 'name').annotate(
            product_count=Count('product'))

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# f
class UniqueProductCountInCategoriesView(generics.ListAPIView):
    serializer_class = UniqueProductCountInCategoriesSerializer

    def get_queryset(self):
        category_ids = self.request.data.get('category_ids', [])

        queryset = Category.objects.filter(id__in=category_ids).annotate(unique_product_count=Count('product',
                                                                                                    distinct=True))

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
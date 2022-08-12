from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer
from .models import Product




@api_view(['GET'])
def apiOverview(request):
    """
    List of all endpoint of Product Api
    """
    api_urls = {
		'List':'/product-list/',
		'Detail View':'/product-detail/<str:pk>/',
		'Create':'/product-create/',
		'Update':'/product-update/<str:pk>/',
		'Delete':'/product-delete/<str:pk>/',
		}

    return Response(api_urls)

@api_view(['GET'])
@cache_page(60**1)
def productList(request):
    """
    Return a list of all the products.

    """
    products = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@cache_page(60*1)
def productDetail(request, pk):
    """
    Return a detail view of existing product.

    """
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
    """
    Add new Products in the database 

    """
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@cache_page(60*60*2)
def productUpdate(request, pk):
    """

    Update the selected product details.

    """
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def productDelete(request, pk):
    """
    Delete product from database.

    """
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Item succsesfully delete!')




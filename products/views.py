from django.http import JsonResponse
from django.shortcuts import render
from .models import *

# The method is for return all products on the platform.
def product_list(request):
    products = Products.objects.all()
    context={
        'products':products,
    }
    return render(request, 'products.html', context)

def api_product_list(request):
    return JsonResponse()

# The method for the seller to the create the product... 
def product_create(request):

    return render(request, 'product_create.html')

def api_product_create(request):
    return JsonResponse()


# Return the product lists based on the user...
def product_list_user(request):
    return render(request, 'products.html')

def api_product_list_user():
    return JsonResponse()

# Add the product to the order.
def product_add_order(request):
    return render(request, 'orders.html')

def api_product_add_order(request):
    return JsonResponse()


# Get the list of orders for buyer and seller.
def product_list_order(request):
    if type=='seller':
        pass
    elif type=='buyer':
        pass
    return render(request, '')

def api_product_list_order(request):
    if type=='seller':
        pass
    elif type=='buyer':
        pass
    return JsonResponse()

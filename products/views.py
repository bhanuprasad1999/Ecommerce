from django.http import JsonResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from .models import *
from users.models import *
from users.views import *

# The method is for return all products on the platform.


@api_view(['GET', 'PUT', 'DELETE'])
@token_authentication
def api_product(request):
    try:
        token_user = Token.objects.filter(
            key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).values()[0]['user_id']
        user_type = UserProfile.objects.filter(
            user__id=token_user).values()[0]['user_type']
        if user_type == 'buyer':
            if request.method == 'GET':
                try:
                    products = Products.objects.all()
                    serializer = ProductSerializer(products, many=True)
                    return JsonResponse({'data': serializer.data})
                except:
                    return JsonResponse({'message': 'No data avaliable'})

        elif user_type == 'seller':
            if request.method == 'GET':
                try:
                    product = Products.objects.filter(
                        product_seller=request.GET['user_id'])
                    serializer = ProductSerializer(products, many=True)
                    return JsonResponse({'data': serializer.data})
                except:
                    return JsonResponse({'message': 'you haven\'t added any products for sale'})

            elif request.method == 'PUT':
                product = Products.objects.get(product_id=request.GET['id'])
                serializer = ProductSerializer(product, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return JsonResponse({'data': 'Successfully updated the product details !'})
        else:
            return JsonResponse({'message': 'Check the type of User you have entered!'})
    except:
        return JsonResponse({'message': 'Authorization required!'})

# The method for the seller to the create the product...


@swagger_auto_schema(method='post', request_body=ProductSerializer)
@api_view(['POST'])
def api_product_edit(request):
    try:
        token_user = Token.objects.filter(
            key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).values()[0]['user_id']
        user_type = UserProfile.objects.filter(
            user__id=token_user).values()[0]['user_type']
        if user_type == 'seller':
            if request.method == 'POST':
                quantity = ProductQuantity.objects.filter(
                    quantity_id=request.data['product_quantity_uom']).exists()
                if quantity:
                    request.data['product_seller'] = token_user
                    serializer = ProductSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return JsonResponse({'message': 'Successfully added a new product'})
                    else:
                        return JsonResponse({'errors': serializer.errors})
                else:
                    return JsonResponse({'message': 'Quantity does not exists!'})
        else:
            return JsonResponse({'message': 'Other than seller no user can create products or sell products'})
    except:
        return JsonResponse({'message': 'Authorization required!'})

# Add the different UOM Quantities


@swagger_auto_schema(method='post', request_body=ProductQuantitySerializer)
@api_view(['POST', 'GET'])
def product_uom_quatity(request):
    try:
        token_user = Token.objects.filter(
            key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).values()[0]['user_id']
        user_type = UserProfile.objects.filter(
            user__id=token_user).values()[0]['user_type']
        if user_type == 'seller':
            try:
                if request.method == 'POST':
                    serializer = ProductQuantitySerializer(request.data)
                    if serializer.is_valid():
                        serializer.save()
                    return JsonResponse({'message': 'Quantity is successfully added!'})
                elif request.method == 'GET':
                    data = ProductQuantity.objects.all()
                    serializer = ProductQuantitySerializer(data, many=True)
                    return JsonResponse({'data': serializer.data})
            except:
                return JsonResponse({'message': 'Something went wrong!'})
        else:
            return JsonResponse({'message': 'Only sellers are applicable!'})
    except:
        return JsonResponse({'message': 'Authorization required!'})


# Add the product to the order.
@api_view(['POST'])
def api_product_add_order(request):
    try:
        if request.method == 'POST':
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Successfully added to your orders!'})
        else:
            return JsonResponse({'message': 'The method is not found!'})
    except:
        return JsonResponse({'error': 'Something went wrong!'})


# Get the list of orders for buyer and seller.
@api_view(['GET', 'DELETE'])
def api_product_list_order(request):
    token_user = Token.objects.filter(
        key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).values()[0]['user_id']
    user_type = UserProfile.objects.filter(
        user__id=token_user).values()[0]['user_type']
    if user_type == 'seller':
        if request.method == 'GET':
            product_orders = Order.objects.filter(
                product_id__product_seller='admin')
            serailizer = OrderSerializer(product_orders, many=True)
            return JsonResponse({'data': serailizer.data})

    elif user_type == 'buyer':
        if request.method == "delete":
            Order.objects.get(order_id=id).delete()
            return JsonResponse({'message': 'The Product is removed from your orders'})

        elif request.method == 'GET':
            product = Order.objects.filter(order_user__id=token_user)
            print(product)
            serializer = OrderSerializer(product, many=True)
            return JsonResponse({'data': serializer.data})

    return JsonResponse({'message': 'Something went wrong!'})

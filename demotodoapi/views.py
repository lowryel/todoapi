from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework.views import Response, APIView
from demotodoapi.serializers import TodoSerializer
from rest_framework.decorators import api_view
from .models import *
from rest_framework import generics
from rest_framework import permissions, authentication
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator




# Create your views here.
@api_view(["GET"])
def index(request):
    # print(request.version)
    instance=Todo.objects.order_by("?").first()
    pages = Paginator(instance, 4)
    data = {}
    if instance:
        data = TodoSerializer(instance).data
    return Response(data)

''' 
    ========== List and/or create apiView ================
'''
class TodoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.TokenAuthentication,
                            authentication.SessionAuthentication]

    method_decorator = (cache_page(60*1))
    method_decorator = vary_on_cookie


''' 
    ========== Retrieve a single apiView ================
'''
class TodoDetailAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,
                            authentication.SessionAuthentication]
    # lookup_url_kwarg = 'pk'



''' 
    ========== Delete apiView ================
'''
class TodoDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication]
    def delete(self, request, **kwargs):
        try:
            queryset = Todo.objects.get(pk=kwargs['pk'])
        except Todo.DoesNotExist:
            raise Http404
        queryset.delete()
        return Response(status=204)
    

''' 
    ========== Update apiView ================
'''
class TodoListUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,
                              authentication.SessionAuthentication]

def products(request):
    # cart = Cart.objects.get(id=1)
    # prod = cart.product.all()
    prod_obj = Product.objects.all()
    print(request.POST)

    context = {
        'prod_obj': prod_obj,
    }
    return render(request, "products.html", context)

def cart(request):
    cart_id = request.session.get('cart_id', None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        cart_obj = qs.first()
        if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save() 
    else:
        # print(cart_obj.user)
        cart_obj = Cart.objects.new(user=request.user)
        request.session['cart_id'] = cart_obj.id

    context = {
        'cart_obj': cart,
    }
    return render(request, 'cart.html', context)




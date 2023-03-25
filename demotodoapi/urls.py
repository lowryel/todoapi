from django.contrib import admin
from django.urls import path, include
from .views import (index,
                    TodoDetailAPIView,
                    TodoListCreateAPIView,
                    TodoDestroyAPIView,
                    TodoListUpdateAPIView,
                    cart,
                    products,
                    )
from rest_framework.authtoken import views

urlpatterns = [
    path("index", index, name="index"),
    path("api/v1/todo/<int:pk>", TodoDetailAPIView.as_view(), name="detailview"),
    path("api/v1/todo/list&create", TodoListCreateAPIView.as_view(), name="createview"),
    path("api/v1/todo/delete/<int:pk>", TodoDestroyAPIView.as_view(), name="deleteview"),
    path("api/v1/todo/update/<int:pk>", TodoListUpdateAPIView.as_view(), name = "updateview"),
    path('api-token-auth/', views.obtain_auth_token),
    path('cart', cart, name='cart'),
    path('products', products, name='products'),
]


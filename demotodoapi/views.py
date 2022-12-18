from django.shortcuts import render
from django.http import Http404
from rest_framework.views import Response, APIView
from demotodoapi.serializers import TodoSerializer
from rest_framework.decorators import api_view
from .models import Todo
from rest_framework import generics
from rest_framework import permissions, authentication


# Create your views here.
@api_view(["GET"])
def index(request, *args, **kwargs):
    instance=Todo.objects.order_by("?").first()
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
        print(kwargs)
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


from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    task = serializers.CharField(max_length=200, validators=[UniqueValidator(queryset=Todo.objects.all(), message="Todo object already in use🤣")])
    user = serializers.StringRelatedField()
    class Meta:
        model = Todo
        fields = "__all__"

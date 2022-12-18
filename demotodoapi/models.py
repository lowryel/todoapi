from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class TodoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user = 1)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=120, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    duration = models.DateTimeField(auto_now=False, null=True)
    done = models.BooleanField(default=False)
    completed = models.DateTimeField(auto_now=False, null=True)
    objects = models.Manager()
    todos = TodoManager() #using (todos) as the model manager instead of (objects)

    def __str__(self):
        return self.task

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance=None, created=False, **kwargs):
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)



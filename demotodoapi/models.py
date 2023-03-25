from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from django.core.translation import gettext as _
# Create your models here.

User = settings.AUTH_USER_MODEL
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


@receiver(post_save, sender=User)
def createAuthToken(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Product(models.Model):
    name = models.CharField(max_length=120, blank = True)
    price = models.IntegerField()
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

class CartManager(models.Manager):
    def new(self, user=None, **kwargs):
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj=user
        return self.model.objects.create(user=user_obj)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    product = models.ManyToManyField(Product, blank = True)
    total = models.DecimalField(decimal_places=2, default=0.00, max_digits=3)
    quantity = models.IntegerField(default=0)
    order_created = models.DateTimeField(auto_now_add=True)
    objects = CartManager()

    # def __int__(self):
    #     return self.total

    # @property
    # def cart_total(self):
    #     total = self.quantity
    #     return total


# @receiver(post_save, sender=Cart)
# def createCartTotal(sender, instance=None, created=False, **kwargs):
#     if created:
#         cart_total = instance.quantity
#         print(created)
#         print(cart_total)
#         return cart_total

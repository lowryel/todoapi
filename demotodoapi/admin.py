from django.contrib import admin
from .models import Todo, Cart, Product

# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("task", "completed", "done")


admin.site.register(Product)
admin.site.register(Cart)

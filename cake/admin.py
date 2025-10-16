from django.contrib import admin
from cake.models import CustomUser, Order, OrderElement, Cake, CakeCategory, Ingredient, Size


class OrderElementsInlines(admin.TabularInline):
    model = OrderElement
    extra = 0

@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    pass

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    inlines = [
        OrderElementsInlines,
    ]
    raw_id_fields = ("user",)

@admin.register(Cake)
class AdminCake(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    pass

@admin.register(Size)
class AdminSize(admin.ModelAdmin):
    pass

@admin.register(CakeCategory)
class AdminCakeCategory(admin.ModelAdmin):
    pass

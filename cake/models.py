from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    tg_id = models.CharField(max_length=150, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.tg_id}"

class CakeCategory(models.Model):
    title=models.CharField(verbose_name="Title",max_length=150,blank=True)
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        max_length=300,
    )
    def __str__(self):
        return self.title

class Ingredient(models.Model):
    title = models.CharField(verbose_name="Title", max_length=150, blank=True)
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        max_length=300,
    )

    def __str__(self):
        return self.title
class Size(models.Model):
    title = models.CharField(verbose_name="Title", max_length=150, blank=True)
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        max_length=300,
    )

    def __str__(self):
        return self.title
class Cake(models.Model):
    title = models.CharField(
        verbose_name='Title',
        blank=True,
        max_length=300,
    )
    image = models.ImageField(
        verbose_name='Image'
    )
    category=models.ForeignKey(
        CakeCategory,
        on_delete=models.CASCADE,
        related_name="cake_categories",
        blank=True,
        null=True,
        verbose_name="Category"
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name="sizes",
        blank=True,
        null=True,
        verbose_name="Size"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="ingredients",
        blank=True,
        null=True,
        verbose_name="Ingredient"
    )
    price = models.IntegerField(verbose_name='Price')
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        max_length=300,
    )
    def __str__(self):
        return self.title



class Order(models.Model):
    class StatusChoice(models.TextChoices):
        DRAFT = "D", "Draft"
        MANAGER = "M", "Transferred to manager"
        RESTAURANT = "R", "Transferred to the restaurant"
        COURIER = "C", "Handed over to the courier"
        PROCESSED = "P", "Processed"

    status = models.CharField(max_length=1, choices=StatusChoice.choices, verbose_name="Статус", db_index=True,
                              default=StatusChoice.DRAFT)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="users",
        verbose_name="User"
    )
    address = models.TextField(verbose_name="Delivery address",blank=True)
    is_draft = models.BooleanField(default=True,verbose_name="Is Draft")
    phone = PhoneNumberField(verbose_name="Phone Number",blank=True)
    email = models.EmailField(max_length=50, blank=True,verbose_name="E-mail")
    def __str__(self):
        return f"{self.user.first_name} | {self.status}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class OrderElement(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Order",
        related_name="orders"
    )
    product = models.ForeignKey(
        Cake,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Product",
        related_name="products"
    )
    price = models.IntegerField(verbose_name="Price",validators=[MinValueValidator(0)], default=0)
    quantity = models.IntegerField(verbose_name="Quantity")

    class Meta:
        verbose_name = 'Order Element'
        verbose_name_plural = 'Order Elements'
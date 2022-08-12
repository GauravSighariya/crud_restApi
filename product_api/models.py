from email.policy import default
from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    


class Product(models.Model):
    category = models.ManyToManyField(Category, blank=False)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, default="Empty description.")
    picture = models.ImageField(default='default.jpg',upload_to="products/images", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    quantity = models.IntegerField(default=10)  # available quantity of given product
    

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

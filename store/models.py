from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=191, blank=False, null=False)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=191, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    product_preview = models.CharField(max_length=191, blank=False, null=False,
                                       verbose_name="Product short description")
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Product description")
    image = models.ImageField(upload_to="product", blank=False, null=False)
    sale_price = models.FloatField(default=0.00, blank=False, null=False)
    previous_price = models.FloatField(default=0.00, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

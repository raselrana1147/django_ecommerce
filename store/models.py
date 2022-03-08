from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


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
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]

    def get_product_url(self):
        return reverse('store:product_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_gallery')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)


class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation='size')

    def colors(self):
<<<<<<< HEAD
        return super(VariationManager, self).filter(variation='color')
=======
        super(VariationManager, self).filter(variation='colors')
>>>>>>> aa6331f497972c41c762ea057a626b9d0d92feaf


VARIATION_TYPE = (
    ('size', 'size'),
    ('color', 'color')
)


class VariationValue(models.Model):
    variation = models.CharField(max_length=191, choices=VARIATION_TYPE)
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects=VariationManager()

    def __str__(self):
        return self.name

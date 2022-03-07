from django.db import models
from django.contrib.auth.models import User
from store.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} X {self.item}"

    def get_total(self):
        total = self.quantity * self.item.sale_price
        float_total = format(total, '0.2f')
        return float_total


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    orderitems=models.ManyToManyField(Cart)
    ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    paymentId=models.CharField(max_length=119,blank=True,null=True)
    orderId=models.CharField(max_length=119,blank=True,null=True)

    def get_totals(self):
        total=0
        for order_item in self.orderitems.all():
            total+=float(order_item.get_total())
        return total



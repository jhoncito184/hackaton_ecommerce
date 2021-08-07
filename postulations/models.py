from django.db import models
from products.models import Product

# Create your models here.
class Postulations(models.Model):
    username = models.TextField()
    phone = models.TextField(max_length=9)
    email = models.TextField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    coupon = models.TextField(editable=False, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username

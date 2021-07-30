from django.db import models
from products.models import Product

# Create your models here.
class Postulations(models.Model):
    username = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username

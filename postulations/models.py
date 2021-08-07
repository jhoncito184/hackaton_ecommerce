from django.db import models
from products.models import Product
import random

def get_promo_code(num_chars):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code

# Create your models here.
class Postulations(models.Model):
    username = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    coupon = models.TextField(default=get_promo_code(5), unique=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username

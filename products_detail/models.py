from django.db import models
from products.models import Product
from schedule.models import Schedule
from modules.models import Modules

# Create your models here.
class ProductDetail(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    title = models.TextField()
    subtitle = models.TextField()
    content_detail = models.TextField()
    image = models.TextField()
    schedule = models.ForeignKey(to=Schedule, on_delete=models.CASCADE)
    modules = models.ForeignKey(to=Modules, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

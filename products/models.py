from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.TextField()
    # image = models.ImageField(upload_to='products', max_length=255, blank=False, null=False, default='-')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

    def __str__(self):
        return self.name

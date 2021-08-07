from django.db import models

# Create your models here.
class Coupon(models.Model):
    email = models.TextField()
    code = models.TextField(editable=False, unique=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.email
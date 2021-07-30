from django.db import models
from authentication.models import User

# Create your models here.
class Benefits(models.Model):
    description = models.TextField()
    title = models.TextField()
    image = models.ImageField(upload_to='benefits', max_length=255, blank=False, null=False, default='-')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.description

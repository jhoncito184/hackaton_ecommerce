from django.db import models

# Create your models here.
class Schedule(models.Model):
    days = models.TextField()
    hours = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

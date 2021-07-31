from django.db import models
from modules.models import Modules

# Create your models here.
class ModulesDetail(models.Model):
    modules = models.ForeignKey(to=Modules, on_delete=models.CASCADE)
    week = models.TextField()
    description = models.TextField()
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

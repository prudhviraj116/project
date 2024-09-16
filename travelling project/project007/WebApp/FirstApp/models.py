from django.db import models

# Create your models here.
class products(models.Model):
    items = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.CharField(max_length=20)
    total = models.FloatField()
    def __str__(self):
        return self.items
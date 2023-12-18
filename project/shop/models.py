from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name

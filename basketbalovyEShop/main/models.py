from django.db import models

class Produkt(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, default="")
    brand = models.ForeignKey('Brand', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} ({self.price})"

class Brand(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.name} ({self.year})"
from django.db import models
from django.db.models.expressions import F
from django.urls import reverse

# Create your models here.
class Medicine(models.Model):
    sku_id = models.CharField(blank=True, null=True, max_length=10)
    product_id = models.CharField(blank=True, null=True, max_length=10)
    sku_name = models.CharField(max_length=50)
    price = models.CharField(blank=True, null=True, max_length=10)
    manufacturer_name = models.CharField(blank=True, null=True,max_length=50)
    salt_name = models.CharField(blank=True, null=True, max_length=20)
    drug_form = models.CharField(max_length=10)
    pack_size = models.CharField(blank=True, null=True, max_length=10)
    strength = models.CharField(blank=True, null=True, max_length=10)
    product_banned = models.CharField(blank=True, null=True, max_length=10)
    unit = models.CharField(blank=True, null=True,max_length=10)
    price_per_unit = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.sku_name

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk':self.pk})

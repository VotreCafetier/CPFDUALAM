from django.db import models

# Create your models here.
class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(unique=True, max_length=255)
    
    def __str__(self):
        return str(self.color_name)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='images/')
    product_price = models.DecimalField(max_digits=16, decimal_places=2)
    color = models.ForeignKey(Color,on_delete=models.CASCADE, null=True)
    product_stock = models.IntegerField(blank=True, null=True)
    product_model = models.CharField(max_length=255, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    product_year_guaranteed = models.SmallIntegerField(blank=True, null=True)
    product_tech_sheet_url = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return str(self.product_name)
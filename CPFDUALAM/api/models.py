from django.db import models
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'
    
    def __str__(self):
        return str(self.city_name)


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    client_lastname = models.CharField(max_length=255)
    client_email = models.EmailField(unique=True, max_length=255)
    address_1 = models.TextField()
    address_2 = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=6)
    client_phone = models.BigIntegerField(blank=True, null=True)
    creation_date = models.DateTimeField()
    country = models.ForeignKey('Country', models.DO_NOTHING)
    city = models.ForeignKey('City', models.DO_NOTHING)
    province = models.ForeignKey('Province', models.DO_NOTHING)
    paiement = models.ForeignKey('Paiement', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client'
    
    def __str__(self):
        return str(self.client_name + " " + self.client_lastname)


class ClientOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    order_date = models.DateTimeField()
    shipping_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey('Orderstatus', models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_order'
    
    def __str__(self):
        return str(self.order_date)


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'color'
    
    def __str__(self):
        return str(self.color_name)


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'country'
    
    def __str__(self):
        return str(self.country_name)


class Orderstatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'orderstatus'
    
    def __str__(self):
        return str(self.status_name)


class Paiement(models.Model):
    paiement_id = models.AutoField(primary_key=True)
    card_number = models.BigIntegerField(unique=True)
    expiration_date = models.SmallIntegerField()
    ccv = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'paiement'
    
    def __str__(self):
        return str(self.card_number)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=16, decimal_places=2)
    color = models.ForeignKey(Color, models.DO_NOTHING)
    product_stock = models.IntegerField(blank=True, null=True)
    product_model = models.CharField(max_length=255, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    product_year_guaranteed = models.SmallIntegerField(blank=True, null=True)
    product_tech_sheet_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
    
    def __str__(self):
        return str(self.product_name)


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    province_name = models.CharField(unique=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'province'
    
    def __str__(self):
        return str(self.province_name)
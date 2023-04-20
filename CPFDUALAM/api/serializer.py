# Serializer is DB to JSON
from .models import *
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city_id','city_name')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id','client_name','client_lastname','client_email','address_1','address_2','postal_code','client_phone','creation_date','country','city','province','paiement')
        depth = 1


class ClientOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrder
        fields = ('order_id','client','product','order_date','shipping_date','status','comments')
        depth = 1


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('color_id','color_name')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_id','country_name')


class OrderstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderstatus
        fields = ('status_id','status_name')


class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = ('paiement_id','card_number','expiration_date','ccv')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id','product_name','product_price','color','product_stock','product_model','product_description','product_year_guaranteed','product_tech_sheet_url')
        depth = 1


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('province_id','province_name')
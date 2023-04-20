from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import *
from .models import *

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientOrderViewSet(viewsets.ModelViewSet):
    queryset = ClientOrder.objects.all()
    serializer_class = ClientOrderSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class OrderstatusViewSet(viewsets.ModelViewSet):
    queryset = Orderstatus.objects.all()
    serializer_class = OrderstatusSerializer

class PaiementViewSet(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
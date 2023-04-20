from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'City', views.CityViewSet)
router.register(r'Client', views.ClientViewSet)
router.register(r'ClientOrder', views.ClientOrderViewSet)
router.register(r'Color', views.ColorViewSet)
router.register(r'Country', views.CountryViewSet)
router.register(r'Orderstatus', views.OrderstatusViewSet)
router.register(r'Paiement', views.PaiementViewSet)
router.register(r'Product', views.ProductViewSet)
router.register(r'Province', views.ProvinceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

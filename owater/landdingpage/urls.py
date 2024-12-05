from django.urls import path

from .utilities import orderProducts
from . import views
from .views import about, contact, detail, home, listOrder, order, orderInfo, orderSuccess, products
urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
     path('products', products, name='products'),
    path('detail/<str:type>', detail, name='detail'),
    path('order', order, name='order'),
    path('order-information', orderInfo, name='orderInfo'),
    path('order-success/<str:idorder>', orderSuccess, name='orderSuccess'),

    path('listOrder', listOrder, name='listOrder'),
    # funtion
    path('order-products', orderProducts, name='orderProducts'),


]
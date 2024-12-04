from django.urls import path

from .utilities import orderProducts
from . import views
from .views import contact, detail, home, order, orderInfo, products
urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
     path('products', products, name='products'),
    path('detail/<str:type>', detail, name='detail'),
    path('order', order, name='order'),
    path('order-information', orderInfo, name='orderInfo'),

    # funtion
    path('order-products', orderProducts, name='orderProducts'),


]
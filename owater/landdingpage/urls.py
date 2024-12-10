from django.urls import path

from .utilities import orderProducts
from . import views
from .views import about, contact, deliveryPolicy, detail, home, listOrder, order, orderInfo, orderSuccess, products, returnPolicy
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
     path('products', products, name='products'),
    path('detail/<str:type>', detail, name='detail'),
    path('order', order, name='order'),
    path('order-information', orderInfo, name='orderInfo'),
    path('order-success/<str:idorder>', orderSuccess, name='orderSuccess'),
     path('delivery-policy', deliveryPolicy, name='deliveryPolicy'),
     path('return-policy', returnPolicy, name='returnPolicy'),

    path('listOrder', listOrder, name='listOrder'),
    # funtion
    path('order-products', orderProducts, name='orderProducts'),

    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="application/xml")),
]
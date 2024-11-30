from django.urls import path
from . import views
from .views import contact, detail, home, order, products
urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
     path('products', products, name='products'),
    path('detail/<str:type>', detail, name='detail'),
    path('order', order, name='order'),
]
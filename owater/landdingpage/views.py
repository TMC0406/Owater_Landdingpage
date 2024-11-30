from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')
def products(request):
    return render(request, 'products.html')
def detail(request,type):
    if type == "A3" :
        return render(request, 'details/detail_A3.html')
    if type == "A2" :
        return render(request, 'details/detail_A2.html')
    if type == "A1" :
        return render(request, 'details/detail_A1.html')
def order(request):
    return render(request, 'order.html')
def contact(request):
    return render(request, 'contact.html')
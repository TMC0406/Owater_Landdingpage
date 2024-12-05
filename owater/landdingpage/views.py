from django.shortcuts import render
from .forms import formInfo
from firebase_admin import firestore
db = firestore.client()

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
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
def listOrder(request):
    listOrder = []
    order_ref = db.collection('orders').stream()
    for item in order_ref :
        data = item.to_dict()
        listOrder.append(data)
    return render(request, 'listOrder.html',{
        "listOrder" : listOrder
    })
def orderSuccess(request ,idorder):
    print("idorder", idorder)
    if not idorder : 
        return 
    requestData = db.collection('orders').document(idorder).get().to_dict()
    return render(request, 'orderSuccess.html',{
        'requestData': requestData,
    })
def contact(request):
    return render(request, 'contact.html')
def orderInfo(request):
    formInfoData = formInfo()
    return render(request, 'orderInfo.html',{
        'formInfoData': formInfoData,
    })
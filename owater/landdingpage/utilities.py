from django.http import JsonResponse
from datetime import datetime, timedelta
from .forms import formInfo
import pytz
vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')
def orderProducts(request): 
    statusreturn = "false"
    if request.method == 'POST':
        print("request.POST",request.POST)
        form = formInfo(request.POST)
        if form.is_valid():
            dataRequest = formInfoData(form)
            print("dataRequest",dataRequest)

            statusreturn = "true"

    return JsonResponse({'statusreturn': statusreturn, 'messageresponse': 'Lỗi phương thức'})
def formInfoData (form):
    current_date = datetime.now(vietnam_tz)
    formatted_date = current_date.strftime("%d/%m/%Y %H:%M:%S")
    timeCreate = formatted_date
    data = {
        'username': form.cleaned_data["username"],
        'phone': form.cleaned_data["phone"],
        'address': form.cleaned_data["address"],
        'province': form.cleaned_data["province"],
        'email': form.cleaned_data["email"],
        'note': form.cleaned_data["note"],
        'createtime': timeCreate,

    }
    return data
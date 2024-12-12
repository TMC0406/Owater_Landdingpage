
from django.http import JsonResponse
from datetime import datetime, timedelta
from .forms import formInfo
import uuid
import pytz
vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')
from firebase_admin import firestore
db = firestore.client()

def orderProducts(request): 
    statusreturn = "false"
    if request.method == 'POST':
        form = formInfo(request.POST)
        if not form.is_valid():
            return JsonResponse({'statusreturn': statusreturn, 'messageresponse': 'Lỗi form'})
        dataRequest = formInfoData(form)

        idorder = generate_short_id()

        dataRequest.update({
            "id" : idorder,
            "status" : "waiting"
        })
        
        print("dataRequest",dataRequest)
        order_ref = db.collection('orders').stream()
        doc_ref = db.collection("orders").document(idorder)
        doc_ref.set(dataRequest, merge = True)
        statusreturn = "true"

        return JsonResponse({'id':idorder,'statusreturn': statusreturn, 'messageresponse': 'Đặt hàng thành công'})
        
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
        'dataOder': form.cleaned_data["dataOder"],
        'createtime': timeCreate,
        'total': form.cleaned_data["total"],

    }
    return data

def generate_short_id():
    # Tạo một chuỗi UUID
    full_id = str(uuid.uuid4())
    # Lấy một phần của chuỗi UUID để có độ dài mong muốn
    short_id = full_id[:8]

    return short_id
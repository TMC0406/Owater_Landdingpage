from django.shortcuts import render

from .forms import formInfo
from firebase_admin import firestore
db = firestore.client()
import json

# Create your views here.
def home(request):
    metaData = {
        "page_description" : "Nước uống Kangen được tạo ra qua quá trình điện giải do người Nhật sáng tạo ra, ngày càng được nhiều người ưa chuộng nhờ vào những lợi ích sức khỏe tuyệt vời mà nó mang lại. Với công nghệ tiên tiến được nhập khẩu từ Nhật Bản, nước uống Kangen OWA có nồng độ ion hydroxide cao, hỗ trợ sức khỏe tổng quát bằng cách giúp cơ thể loại bỏ các gốc tự do có hại. Điều này giúp ngăn ngừa quá trình lão hóa, tăng cường hệ miễn dịch và giảm nguy cơ mắc các bệnh mãn tính như tiểu đường và bệnh tim mạch.",
        "page_og_url" : "https://www.owa.vn/",
        "page_keywords" : 'nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe ',
        "page_title" : "OWA Vietnam",
        "page_image" : "https://www.owa.vn/static/assets/imgs/banners/Banner_Social.webp",
    }
    return render(request, 'home.html',{
        "metaData" : metaData
    })
def about(request):
    metaData = {
        "page_description" : "Công ty TNHH OWA Việt Nam là doanh nghiệp tiên phong trong lĩnh vực nước uống Kangen tại thị trường Việt Nam. Vời chất lượng nước ion kiềm số 1 thị trường Việt Nam, chúng tôi cam kết mang tới sản phẩm nước ion kiềm chất lượng cao, được sản xuất theo tiêu chuẩn quốc tế, với độ pH lên tới 9,5 và nồng độ ion hydroxide cao, giúp cân bằng độ pH trong cơ thể. Theo nghiên cứu của học viện Y khoa Hoa Kỳ, nước ion kiềm cùng với các nguyên tố vi lượng kết hợp có tác dụng tích cực cho sức khỏe.",
        "page_og_url" : "https://www.owa.vn/about",
        "page_keywords" : 'nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe ',
        "page_title" : "Về OWA",
        "page_image" : "https://www.owa.vn/static/assets/imgs/banners/Banner_Social.webp",
    }
    return render(request, 'about.html',{
        "metaData" : metaData
    })
def products(request):
    metaData = {
        "page_description" : "Nước uống Kangen được tạo ra qua quá trình điện giải do người Nhật sáng tạo ra, ngày càng được nhiều người ưa chuộng nhờ vào những lợi ích sức khỏe tuyệt vời mà nó mang lại. Với công nghệ tiên tiến được nhập khẩu từ Nhật Bản, chúng tôi xin giới thiệu đến bạn các sản phẩm nước uống ion kiềm chất lượng cao của mình.",
        "page_og_url" : "https://www.owa.vn/products",
        "page_keywords" : 'nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe ',
        "page_title" : "Sản Phẩm",
        "page_image" : "https://www.owa.vn/static/assets/imgs/Slide_4_fulltext.webp",
    }
    return render(request, 'products.html',{
        "metaData" : metaData
    })

def deliveryPolicy(request):
    metaData = {
        "page_description" : "Chính sách giao hàng",
        "page_og_url" : "https://www.owa.vn/",
        "page_keywords" : 'nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe ',
        "page_title" : "Chính sách giao hàng",
        "page_image" : "https://www.owa.vn/static/assets/imgs/banners/Untitled-2.webp",
    }
    return render(request, 'seemore/delivery_policy.html',{
        "metaData" : metaData
    })
def returnPolicy(request):
    metaData = {
        "page_description" : "Chính sách đổi trả hàng.",
        "page_og_url" : "https://www.owa.vn/return-policy",
        "page_keywords" : 'nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe ',
        "page_title" : "Chính sách đổi trả hàng",
        "page_image" : "https://www.owa.vn/static/assets/imgs/banners/Untitled-2.webp",
    }
    return render(request, 'seemore/return_policy.html',{
        "metaData" : metaData
    })
def detail(request,type):
    if type == "A3" :
        metaData = {
            "page_description" : "NƯỚC UỐNG KANGEN OWA TYPE A3 - PH 8.0-8.5. Giá bán: 45.000đ. Owarter bình 20L là loại nước cao cấp, khoáng chất hoàn toàn tự nhiên. Có nồng độ pH nhẹ, vị ngọt thanh mát, phù hợp cho người mới bắt đầu sử dụng nước ion kiềm.",
            "page_og_url" : "https://www.owa.vn/detail/A3",
            "page_keywords" :"nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe, Calcium: 80, Magnesium: 40, Potassium: 2, Sodium: 6.5, Nitrates: 3.8, Bicarbonates: 360, Sulfates: 3, Silica: 10, Chloride:s 0.7, PH: 8.0-8.5 ",
            "page_title" : "NƯỚC UỐNG KANGEN OWA TYPE A3",
            "page_image" : "https://www.owa.vn/static/assets/imgs/products/Binh%20nuoc%20A3.webp",
        }
        return render(request, 'details/detail_A3.html',{
        "metaData" : metaData
    })
    if type == "A2" :
        metaData = {
             "page_description" : "NƯỚC UỐNG KANGEN OWA TYPE A2 - PH 8.5-8.9. Giá bán: 65.000đ. Owarter bình 20L là loại nước cao cấp, khoáng chất hoàn toàn tự nhiên. Có độ pH vừa, vị ngọt thanh mát, giúp trung hòa các gốc axit trong cơ thể, cân bằng pH.",
            "page_og_url" : "https://www.owa.vn/detail/A2",
            "page_keywords" :"nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe,Calcium: 80, Magnesium: 40, Potassium: 2, Sodium: 6.5, Nitrates: 3.8, Bicarbonates: 360, Sulfates: 3, Silica: 10, Chloride:s 0.7, PH: 8.5-8.9.",
            "page_title" : "NƯỚC UỐNG KANGEN OWA TYPE A2",
            "page_image" : "https://www.owa.vn/static/assets/imgs/products/Binh%20nuoc%20A2.webp",
        }
        return render(request, 'details/detail_A2.html',{
        "metaData" : metaData
    })
    if type == "A1" :
        metaData = {
           "page_description" : "NƯỚC UỐNG KANGEN OWA TYPE A1 - PH 9.0-9.5. Giá bán: 100.000đ. Owarter bình 20L là loại nước cao cấp, khoáng chất hoàn toàn tự nhiên. Đặc biệt tốt cho cơ thể với độ pH cao, nồng độ ion hydroxide cao, vị ngọt thanh mát, trung hòa các gốc axit có hại, tốt cho người bị axit dạ dày, gout, và các bệnh liên quan đến axit dư thừa.",
            "page_og_url" : "https://www.owa.vn/detail/A1",
            "page_keywords" : "nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe,Calcium: 80, Magnesium: 40, Potassium: 2, Sodium: 6.5, Nitrates: 3.8, Bicarbonates: 360, Sulfates: 3, Silica: 10, Chloride:s 0.7, PH:  9.0-9.5",
            "page_title" : "NƯỚC UỐNG KANGEN OWA TYPE A1",
            "page_image" : "https://www.owa.vn/static/assets/imgs/products/Binh%20nuoc.webp",
        }
        return render(request, 'details/detail_A1.html',{
        "metaData" : metaData
    })
def order(request):
    metaData = {
        "page_description" : "OWA Vietnam Co., Ltd - Chuyên cung cấp nước uống tinh khiết, đảm bảo chất lượng và an toàn cho sức khỏe. Sự lựa chọn hàng đầu cho gia đình và doanh nghiệp.",
        "page_og_url" : "https://www.owa.vn/",
        "page_keywords" : "nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe,",
        "page_title" : "OWA Vietnam",
        "page_image" : "https://www.owa.vn/static/assets/imgs/banners/Banner_Social.webp",
    }
    return render(request, 'order.html',{
        "metaData" : metaData
    })
def listOrder(request):
    listOrder = []
    order_ref = db.collection('orders').stream()
    for item in order_ref :
        data = item.to_dict()
        id = data['id']
        dataOder =[]
        product_ref = db.collection("orders").document(id).collection("products").stream()
        for itemproduct in product_ref :
            dataOder.append(itemproduct.to_dict())
        data.update({
            "dataOder" : dataOder ,
            })
        print (data)
        listOrder.append(data)
    return render(request, 'listOrder.html',{
        "listOrder" : listOrder,
    })

def orderSuccess(request ,idorder):
    print("idorder", idorder)
    if not idorder : 
        return 
    requestData = db.collection('orders').document(idorder).get().to_dict()
    product_ref = db.collection("orders").document(idorder).collection("products").stream()
    dataOder = []
    for itemproduct in product_ref :
        dataOder.append(itemproduct.to_dict())
    requestData.update({
        "dataOder" : dataOder ,
        })
    print("requestData",requestData)
    metaData = {
        "page_description" : "OWA Vietnam Co., Ltd - Chuyên cung cấp nước uống tinh khiết, đảm bảo chất lượng và an toàn cho sức khỏe. Sự lựa chọn hàng đầu cho gia đình và doanh nghiệp.",
        "page_og_url" : "https://www.owa.vn/",
        "page_keywords" : "nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe,",
        "page_title" : "Thông tin đơn hàng",
        "page_image" : "https://www.owa.vn/static/assets/imgs/banners/Banner_Social.webp",
    }
    return render(request, 'orderSuccess.html',{
        'requestData': requestData,
        "metaData" : metaData
    })
def contact(request):
    metaData = {
        "page_description" : "Địa chỉ: Tầng 1 Tòa nhà i9 Khuất Duy Tiến, Phường Thanh Xuân Bắc, Quận Thanh Xuân, Hanoi, Vietnam,Facebook: https://www.facebook.com/OWAHighOxygen,Gmail: owavietnam@gmail.com,Số điện thoại: 1900 8942 ",
        "page_og_url" : "https://www.owa.vn/",
        "page_keywords" : "OWA Vietnam Co., Ltd - Chuyên cung cấp nước uống tinh khiết, đảm bảo chất lượng và an toàn cho sức khỏe. Sự lựa chọn hàng đầu cho gia đình và doanh nghiệp.",
        "page_title" : "Liên hệ",
        "page_image" : "https://www.owa.vn/static/assets/imgs/image_contact.webp",
    }
    return render(request, 'contact.html',{
        "metaData" : metaData
    })
def orderInfo(request):
    formInfoData = formInfo()
    metaData = {
        "page_description" : "OWA Vietnam Co., Ltd - Chuyên cung cấp nước uống tinh khiết, đảm bảo chất lượng và an toàn cho sức khỏe. Sự lựa chọn hàng đầu cho gia đình và doanh nghiệp.",
        "page_og_url" : "https://www.owa.vn/",
        "page_keywords" : "nước kangen, nước owa, nước tốt cho sức khỏe,kangen, owa, owarte , i-on kiềm ,  OWA HIGH OXYGEN, Độ pH cao lên đến 9.5, Nồng độ i-on Hydroxide cao, Nguồn gốc tự nhiên, Độ tinh khiết cao,pH ổn định, Không xử lý hóa học, Hỗ trợ sức khỏe",
        "page_title" : "Thông tin đặt hàng",
        "page_image" : "https://www.owa.vn/static/assets/imgs/banners/Banner_Social.webp",
    }
    return render(request, 'orderInfo.html',{
        'formInfoData': formInfoData,
        "metaData" : metaData
    })









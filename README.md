# Owater_Landdingpage

# Tạo môi trường ảo
python3 -m venv django-env

# Kích hoạt môi trường ảo
source django-env/bin/activate

# Cài đặt Django
python3 -m pip install django

# Cài đặt các thư viện bổ sung
source django-env/bin/activate
pip3 install firebase-admin
pip3 install pytz
pip3 install openpyxl
pip3 install djangorestframework

# Chuyển vào thư mục dự án
cd owater
# Chạy các lệnh migrate
python manage.py migrate
# Chạy server để kiểm tra
python manage.py runserver

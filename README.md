# Chatbot chẩn đoán bệnh cây mai vàng (Baseline)

Mục tiêu
Xây dựng chatbot cơ bản có thể:

- Nhận mô tả triệu chứng từ người dùng
- Gợi ý loại bệnh và cách xử lý
- Cho phép tải ảnh minh họa (chưa có AI nhận diện)
- Là nền tảng cho việc phát triển mô hình chẩn đoán bằng hình ảnh sau này

##Cách cài và chạy
##Cần chạy trong môi trường venv
###Chạy lệnh cài môi trường (nếu chưa có)
python -m venv .env
source .env/bin/activate

###Cài đặt thư viện cần thiết

pip install streamlit pillow

import streamlit as st
from PIL import Image
import random
import time
from diseases import diseases_data

# --- Cấu hình ---
st.set_page_config(page_title="Chatbot Mai Vàng", page_icon="🌼")
st.title("Chat Mai Vàng – Chẩn đoán & Tư vấn cơ bản")
st.write("Phiên bản baseline: mô phỏng nhận diện ảnh + trò chuyện cơ bản.\n")
# --- Upload ảnh ---
st.subheader("📷 Chẩn đoán qua ảnh")
uploaded_file = st.file_uploader("Tải ảnh cây mai bị bệnh", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Ảnh cây mai bạn tải lên", use_container_width=True)

    st.write("🔄 Đang phân tích ảnh...")
    with st.spinner("Đang mô phỏng mô hình AI..."):
        time.sleep(2)

        ten_benh = random.choice(list(diseases_data.keys()))
        chi_tiet = diseases_data[ten_benh]

        st.success(f" Có thể cây bị: **{ten_benh}**")
        st.write(f"**Nguyên nhân:** {chi_tiet['nguyên nhân']}")
        st.write(f"**Cách xử lý:** {chi_tiet['cách xử lý']}")

    # #result = random.choice(diseases_data)
    # result = random.choice(list(diseases_data.values()))

    # st.success(f" Có thể cây bị: **{result['tên']}**")
    # st.write(f" **Nguyên nhân:** {result['nguyên nhân']}")
    # st.write(f" **Cách xử lý:** {result['cách xử lý']}")

st.markdown("---")

# --- Chatbot mô phỏng ---
st.subheader("💬 Trò chuyện với chatbot ")
# --- Nhập mô tả triệu chứng ---
symptom_input = st.text_input("👉 Nhập mô tả triệu chứng (ví dụ: lá vàng, rễ thối, nụ rụng...)")
if st.button("🔍 Chẩn đoán"):
    if symptom_input.strip() == "" :
        st.warning("⚠️ Vui lòng nhập mô tả ")
    else:
        found = False
        for symptom, info in diseases_data.items():
            if symptom in symptom_input.lower():
                st.success(f"🩺 Có thể cây bị: **{symptom}**")
                st.write(f"🌿 **Nguyên nhân:** {info['nguyên nhân']}")
                st.write(f"💊 **Cách xử lý:** {info['cách xử lý']}")
                found = True
                break

        if not found:
            st.info("❓ Chatbot chưa có thông tin về triệu chứng này.")
# if "chat_histo" not in st.session_state:
#     st.session_state.chat_histo = []  # khởi tạo danh sách trống để lưu tin nhắn

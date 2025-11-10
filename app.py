# app.py
import streamlit as st
from diseases import diseases_data
from PIL import Image

# --- Cấu hình giao diện ---
st.set_page_config(page_title="Chatbot Mai Vàng", page_icon="🌼")
st.title("🌼 Chatbot chẩn đoán bệnh trên cây mai vàng")
st.write("Công cụ hỗ trợ người trồng mai xác định bệnh thường gặp và cách xử lý cơ bản.\n")

# --- Nhập mô tả triệu chứng ---
symptom_input = st.text_input("👉 Nhập mô tả triệu chứng (ví dụ: lá vàng, rễ thối, nụ rụng...)")

# --- Upload ảnh ---
uploaded_file = st.file_uploader("📷 Hoặc tải ảnh cây mai (chưa nhận diện tự động, chỉ hiển thị minh họa)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Ảnh cây mai bạn tải lên", use_container_width=True)

# --- Nút chẩn đoán ---
if st.button("🔍 Chẩn đoán"):
    if symptom_input.strip() == "" and not uploaded_file:
        st.warning("⚠️ Vui lòng nhập mô tả hoặc tải ảnh.")
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
            st.info("❓ Chatbot chưa có thông tin về triệu chứng này. (Phần AI nhận diện ảnh sẽ được phát triển ở bước sau 🌱)")

st.markdown("---")
st.caption("💡 Phiên bản baseline: demo ý tưởng. Phiên bản hoàn chỉnh sẽ có nhận diện hình ảnh và học máy tự động.")

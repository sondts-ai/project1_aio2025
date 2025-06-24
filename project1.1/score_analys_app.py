import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import io
from PIL import Image

# Tiêu đề ứng dụng
st.title("Phân tích dữ liệu diểm số học sinh")
# Upload file
uploaded_file = st.file_uploader('Chọn file Excel (có cột "điểm số")', type=["xlsx"])


# Tính điểm trung bình
def caculus_avg(scores):
    return sum(scores) / len(scores)


# Phân loại điểm số
def persentage_distribution(scores):
    bins = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0, "<60": 0}
    for score in scores:
        if score >= 90:
            bins["90-100"] += 1
        elif score >= 80:
            bins["80-89"] += 1
        elif score >= 70:
            bins["70-79"] += 1
        elif score >= 60:
            bins["60-69"] += 1
        else:
            bins["<60"] += 1
    return bins


# Khi có file
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    scores = df["điểm số"].dropna().astype(float).tolist()
    if scores:
        st.write(
            "Tổng số học sinh:",
            len(scores),
            "Điểm trung bình:",
            round(caculus_avg(scores), 2),
        )
        # Phân loại điểm
        dist = persentage_distribution(scores)
        labels = list(dist.keys())
        values = list(dist.values())

        fig, ax = plt.subplots(figsize=(7, 7))
        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            textprops={"fontsize": 10},
            startangle=70
        )
        ax.axis('equal')  # Đảm bảo biểu đồ tròn
        ax.set_title("Biểu đồ phân bố điểm số", fontsize=12)
        
        # Hiển thị trực tiếp bằng st.pyplot()
        st.pyplot(fig)

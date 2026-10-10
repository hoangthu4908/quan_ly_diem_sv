import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# 1. Tạo dữ liệu mẫu trực tiếp với tên cột bằng Tiếng Việt có dấu
data = {
    "Họ và tên": [
        "An",
        "Hương",
        "Lan",
        "Minh",
        "Bình",
        "Hiền",
        "Trang",
        "Bảo",
        "Trâm",
        "My",
    ],
    "Chuyên cần": [8.0, 9.0, 7.5, 8.5, 9.5, 7.0, 6.5, 9.5, 7.0, 9.0],
    "Giữa kỳ": [7.0, 8.0, 7.5, 6.0, 9.0, 9.5, 8.5, 7.5, 9.0, 8.5],
    "Cuối kỳ": [8.0, 8.5, 9.0, 9.0, 7.0, 8.5, 9.5, 7.0, 7.5, 9.0],
}

df = pd.DataFrame(data)
df.index = range(1, len(df) + 1)

# 2. Tính điểm tổng kết
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"] + 0.3 * df["Giữa kỳ"] + 0.5 * df["Cuối kỳ"]
).round(2)


# 3. Hàm xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 4. Giao diện Web App Streamlit
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm của 10 sinh viên")
st.dataframe(df)  # Hiển thị hoàn toàn tiếng Việt có dấu chuẩn

st.subheader("Thống kê chung")
dtb_lop = df["Tổng kết"].mean()
sv_max = df.loc[df["Tổng kết"].idxmax()]
sv_min = df.loc[df["Tổng kết"].idxmin()]
so_dat = (df["Tổng kết"] >= 5.0).sum()

st.write(f"- **Điểm tổng kết trung bình của lớp:** {dtb_lop:.2f}")
st.write(
    f"- **Sinh viên có điểm cao nhất:** {sv_max['Họ và tên']} ({sv_max['Tổng kết']})"
)
st.write(
    f"- **Sinh viên có điểm thấp nhất:** {sv_min['Họ và tên']} ({sv_min['Tổng kết']})"
)
st.write(f"- **Số sinh viên đạt (>= 5.0):** {so_dat}")

st.subheader("Tra cứu thông tin cá nhân sinh viên")
ten_chon = st.selectbox("Chọn tên sinh viên:", df["Họ và tên"])
sv_chon = df[df["Họ và tên"] == ten_chon].iloc[0]

st.write(f"**Họ và tên:** {sv_chon['Họ và tên']}")
st.write(f"- Điểm chuyên cần: {sv_chon['Chuyên cần']}")
st.write(f"- Điểm giữa kỳ: {sv_chon['Giữa kỳ']}")
st.write(f"- Điểm cuối kỳ: {sv_chon['Cuối kỳ']}")
st.write(f"- **Điểm tổng kết:** {sv_chon['Tổng kết']}")
st.write(f"- **Xếp loại:** {sv_chon['Xếp loại']}")

st.subheader("Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 4))
# Dùng chuỗi không dấu riêng cho trục X của biểu đồ để tránh lỗi font trên Linux/Streamlit Cloud
ten_khong_dau = [
    "An",
    "Huong",
    "Lan",
    "Minh",
    "Binh",
    "Hien",
    "Trang",
    "Bao",
    "Tram",
    "My",
]
ax.bar(ten_khong_dau, df["Tổng kết"], color="orange")
ax.set_xlabel("Sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_ylim(0, 10)

for i, txt in enumerate(df["Tổng kết"]):
    ax.annotate(str(txt), (ten_khong_dau[i], df["Tổng kết"].iloc[i] + 0.1), ha="center")

st.pyplot(fig)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: small;'>Họ tên: Hoàng Anh Thư - MSSV: 026308009340</p>",
    unsafe_allow_html=True,
)

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# 1. Tạo dữ liệu mẫu
data = {
    "Ho_va_ten": [
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
    "Chuyen_can": [8.0, 9.0, 7.5, 8.5, 9.5, 7.0, 6.5, 9.5, 7.0, 9.0],
    "Giua_ky": [7.0, 8.0, 7.5, 6.0, 9.0, 9.5, 8.5, 7.5, 9.0, 8.5],
    "Cuoi_ky": [8.0, 8.5, 9.0, 9.0, 7.0, 8.5, 9.5, 7.0, 7.5, 9.0],
}

df = pd.DataFrame(data)
df.index = range(1, len(df) + 1)

# 2. Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"] + 0.3 * df["Giua_ky"] + 0.5 * df["Cuoi_ky"]
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


df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 4. Giao diện Web App Streamlit
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm của 10 sinh viên")
st.dataframe(df)

st.subheader("Thống kê chung")
dtb_lop = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_dat = (df["Tong_ket"] >= 5.0).sum()

st.write(f"- **Điểm tổng kết trung bình của lớp:** {dtb_lop:.2f}")
st.write(
    f"- **Sinh viên có điểm cao nhất:** {sv_max['Ho_va_ten']} ({sv_max['Tong_ket']})"
)
st.write(
    f"- **Sinh viên có điểm thấp nhất:** {sv_min['Ho_va_ten']} ({sv_min['Tong_ket']})"
)
st.write(f"- **Số sinh viên đạt (>= 5.0):** {so_dat}")

st.subheader("Tra cứu thông tin cá nhân sinh viên")
ten_chon = st.selectbox("Chọn tên sinh viên:", df["Ho_va_ten"])
sv_chon = df[df["Ho_va_ten"] == ten_chon].iloc[0]

st.write(f"**Họ và tên:** {sv_chon['Ho_va_ten']}")
st.write(f"- Điểm chuyên cần: {sv_chon['Chuyen_can']}")
st.write(f"- Điểm giữa kỳ: {sv_chon['Giua_ky']}")
st.write(f"- Điểm cuối kỳ: {sv_chon['Cuoi_ky']}")
st.write(f"- **Điểm tổng kết:** {sv_chon['Tong_ket']}")
st.write(f"- **Xếp loại:** {sv_chon['Xep_loai']}")

st.subheader("Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df["Ho_va_ten"], df["Tong_ket"], color="orange")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

# Hiển thị giá trị lên trên cột biểu đồ
for i, txt in enumerate(df["Tong_ket"]):
    ax.annotate(
        str(txt),
        (df["Ho_va_ten"].iloc[i], df["Tong_ket"].iloc[i] + 0.1),
        ha="center",
    )

st.pyplot(fig)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: small;'>Họ tên: Hoàng Anh Thư - MSSV: 026308009340</p>",
    unsafe_allow_html=True,
)

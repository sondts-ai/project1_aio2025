import streamlit as st
from factorial import fact
import os


def user_load():
    # Đọc danh sách từ file txt
    try:
        if os.path.exists("user.txt"):
            with open("user.txt", "r", encoding="utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
            return users
        else:
            st.error("File user.txt không tồn tại")
            return []
    except Exception as e:
        st.error(f"Lỗi đọc file:{e}")
        return []


def login_page():
    # Trang đăng nhâp
    st.title("Đăng nhập")
    # input user
    user_name = st.text_input("Nhập tên người dùng")
    if st.button("Đăng nhập"):
        if user_name:
            users = user_load()
            if user_name in users:
                st.session_state.logged_in = True
                st.session_state.user_name = user_name
                st.rerun()
            # Nếu user không hợp lệ hiện trang chào hỏi
            else:
                st.session_state.show_greeting = True
                st.session_state.user_name = user_name
                st.rerun()
        else:
            st.warning("Vui lòng nhập user_name")


def factorial_caculus():
    st.title("Tính toán giai thừa")
    # Hiển thị thông tin người đăng nhập
    st.write(f"Xin chào,{st.session_state.user_name}!")
    # Nút đăng xuât
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        st.rerun()

    st.divider()

    number = st.number_input("Enter a number:", min_value=0, max_value=90)
    if st.button("Caculus"):
        result = fact(number)
        st.write(f"Gia thừa của {number} là:{result}")


def greeting_page():
    # Xây dựng trang cho user không hợp lệ
    st.title("Xin chào")
    st.write(f"Xin chào,{st.session_state.user_name}")
    st.write("Bạn không có quyền truy cập")
    if st.button("Quay lại "):
        st.session_state.show_greeting = False
        st.session_state.user_name = ""
        st.rerun()


def main():
    # Khởi tạo season state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""
    if "show_greeting" not in st.session_state:
        st.session_state.show_greeting = False
    # Điều hướng trang dựa trên trạng thái đăng nhập
    if st.session_state.logged_in:
        factorial_caculus()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()


if __name__ == "__main__":
    main()

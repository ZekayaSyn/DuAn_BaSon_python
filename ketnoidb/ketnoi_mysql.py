import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """Hàm kết nối MySQL và trả về đối tượng connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',      # Tên máy chủ (VD: 127.0.0.1)
            user='root',           # Tên đăng nhập MySQL
            password='',           # Mật khẩu MySQL
            database='qlbanquanaozek'   # Tên database bạn muốn dùng
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi kết nối MySQL:", e)
        return None

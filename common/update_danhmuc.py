from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql


def update_danhmuc(madm, tendm_moi, mota_moi):

    try:
        connection = connect_mysql()
        if connection is None:
            print("Không thể kết nối CSDL.")
            return
        cursor = connection.cursor()
        sql = "UPDATE danhmuc SET tendm = %s, mota = %s WHERE madm = %s"
        data = (tendm_moi, mota_moi, madm)
        cursor.execute(sql, data)
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục mã {madm} thành công!")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã {madm} để cập nhật.")

    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
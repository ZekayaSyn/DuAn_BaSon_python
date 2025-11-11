from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def delete_danhmuc(madm):
    try:
        connection = connect_mysql()
        if connection is None:
            print("Không thể kết nối CSDL.")
            return
        cursor = connection.cursor()
        sql = "DELETE FROM danhmuc WHERE madm = %s"
        cursor.execute(sql, (madm,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có mã {madm} thành công!")
        else:
            print(f"⚠️ Không tìm thấy danh mục có mã {madm}.")

    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


def get_all_danhmuc():
    try:
        connection = connect_mysql()
        if connection is None:
            print("Không thể kết nối CSDL.")
            return []

        cursor = connection.cursor(dictionary=True)  # Trả về dạng dict (key: value)
        sql = "SELECT * FROM danhmuc ORDER BY madm ASC"
        cursor.execute(sql)
        danhmuc_list = cursor.fetchall()

        if danhmuc_list:
            print("✅ Danh sách danh mục:")
            for dm in danhmuc_list:
                print(f"{dm['madm']}: {dm['tendm']} - {dm['mota']}")
        else:
            print("⚠️ Không có danh mục nào trong CSDL.")

        return danhmuc_list

    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
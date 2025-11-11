
from zoneinfo._common import load_data
from common.delete_danhmuc import delete_danhmuc
from common.insertdanhmuc import insert_danhmuc
from common.update_danhmuc import update_danhmuc
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql

# --- HÀM THÊM ---
def insert_danhmuc():
    tendm = entry_tendm.get()
    mota = entry_mota.get()
    if not tendm:
        messagebox.showwarning("Cảnh báo", "Tên danh mục không được để trống!")
        return

    connection = connect_mysql()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)"
        cursor.execute(sql, (tendm, mota))
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")
        load_data()
        entry_tendm.delete(0, tk.END)
        entry_mota.delete(0, tk.END)


# --- HÀM XÓA ---
def delete_danhmuc():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Hãy chọn một danh mục để xóa!")
        return
    madm = tree.item(selected, "values")[0]

    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa danh mục này?"):
        connection = connect_mysql()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM danhmuc WHERE madm = %s", (madm,))
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Thành công", "Đã xóa danh mục!")
            load_data()


# --- HÀM CẬP NHẬT ---
def update_danhmuc():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Cảnh báo", "Hãy chọn danh mục để cập nhật!")
        return
    madm = tree.item(selected, "values")[0]
    tendm = entry_tendm.get()
    mota = entry_mota.get()

    if not tendm:
        messagebox.showwarning("Cảnh báo", "Tên danh mục không được để trống!")
        return

    connection = connect_mysql()
    if connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE danhmuc SET tendm=%s, mota=%s WHERE madm=%s", (tendm, mota, madm))
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Thành công", "Đã cập nhật danh mục!")
        load_data()

def select_item(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        entry_tendm.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        entry_tendm.insert(0, values[1])
        entry_mota.insert(0, values[2])
# --- HÀM LẤY DỮ LIỆU ---
def load_data():
    for row in tree.get_children():
        tree.delete(row)
    connection = connect_mysql()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM danhmuc ORDER BY madm ASC")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
        cursor.close()
        connection.close()
root = tk.Tk()
root.title("Quản lý danh mục sản phẩm")
root.geometry("700x500")
root.resizable(False, False)

# --- FRAME NHẬP LIỆU ---
frame_input = tk.LabelFrame(root, text="Thông tin danh mục", padx=10, pady=10)
frame_input.pack(fill="x", padx=10, pady=10)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, sticky="w")
entry_tendm = tk.Entry(frame_input, width=30)
entry_tendm.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, sticky="w")
entry_mota = tk.Entry(frame_input, width=30)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# --- FRAME NÚT ---
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

btn_add = tk.Button(frame_buttons, text="Thêm", width=12, bg="#4CAF50", fg="white", command=insert_danhmuc)
btn_add.grid(row=0, column=0, padx=5)

btn_update = tk.Button(frame_buttons, text="Sửa", width=12, bg="#FFC107", command=update_danhmuc)
btn_update.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="Xóa", width=12, bg="#F44336", fg="white", command=delete_danhmuc)
btn_delete.grid(row=0, column=2, padx=5)

btn_reload = tk.Button(frame_buttons, text="Làm mới", width=12, command=load_data)
btn_reload.grid(row=0, column=3, padx=5)

# --- BẢNG HIỂN THỊ DANH MỤC ---
columns = ("madm", "tendm", "mota")
tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
tree.pack(fill="both", expand=True, padx=10, pady=10)

tree.heading("madm", text="Mã DM")
tree.heading("tendm", text="Tên danh mục")
tree.heading("mota", text="Mô tả")

tree.column("madm", width=60, anchor="center")
tree.column("tendm", width=200)
tree.column("mota", width=380)

tree.bind("<<TreeviewSelect>>", select_item)

# --- CHẠY ---
load_data()
root.mainloop()
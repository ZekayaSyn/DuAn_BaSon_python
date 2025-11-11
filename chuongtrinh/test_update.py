from common.update_danhmuc import update_danhmuc
while True:
    madm=input("Mã danh mục")
    ten=input("Nhập vào tên danh mục")
    mota=input("Nhập vào mô tả")
    update_danhmuc(madm,ten,mota)
    con=input("Tiếp tục y, Thoát thì nhân kí tự bất kỳ")
    if con!="y":
        break

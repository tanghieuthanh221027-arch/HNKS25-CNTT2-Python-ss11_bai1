# code đã sửa
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

product_id = product_info[0]
product_name = product_info[1]
product_size = product_info[2]

product_info_list = list(product_info)
product_info_list[3] = 279000
product_info = tuple(product_info_list)


print(f'''
Mã sản phẩm : {product_id}
Tên sản phẩm : {product_name}
Số lượng thông tin sản phẩm : {len(product_info)}
Thông tin sau khi cập nhật : {product_info}''')

# tuple product_info ban đầu có 4 phần tử 
# phần tử 'SP001' nằm ở index 0 nên dòng code này sai : product_id = product_info[1] (lấy nhầm product_name)
# phần tử 'Áo polo nam' nằm ở index 1 nên dòng code này sai : product_name = product_info[2] (lấy nhầm product_size)
# product_length = product_info.length() dòng này sai vì trong python không có hàm length() , nếu muốn dùng để tìm độ dài của list thì nên dùng len(product_info)
# product_info[3] = 279000 dòng code này không hợp lệ vì product_info là 1 tuple mang tính immutable , không thể sửa hay thay đổi trực tiếp được , nên muốn cập nhật giá tiền thì dùng cách sau : 
# product_info_list = list(product_info)
# product_info_list[3] = 279000
# product_info = tuple(product_info_list)
# chuyển tuple về dạng list để cập nhật giá tiền , sau khi cập nhật xong thì thay đổi lại kiểu dữ liệu là tuple 

# Thư viện Marshmallow để hỗ trợ quá trình serialize
# (chuyển đổi đối tượng Python thành định dạng JSON)
# và deserialize (ngược lại) dữ liệu.

from .extension import ma

# Chuyển đổi sang JSON và ngược lại
class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id','users','password')

#Lớp BooksSchema kế thừa từ ma.Schema. Bên trong lớp Meta, thuộc tính fields định nghĩa
# các trường (fields) của đối tượng sách mà bạn muốn serialize/deserialize
class BooksSchema(ma.Schema):
    class Meta:
        fields=('id','ten','soTrang')
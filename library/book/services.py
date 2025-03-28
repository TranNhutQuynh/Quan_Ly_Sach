#Logic Nghiệp vụ (business logic)

from library.extension import db
from library.library_ma import BooksSchema
from library.models import Books,Author
from flask import request,jsonify

#khởi tạo đối tượng Schema
book_Schema=BooksSchema()   #lấy 1 quyển sách
books_Schema=BooksSchema(many=True) #lấy nhiều quyển sách

def add_book_services():
    #lấy dữ liệu từ request
    data=request.json

    if (data and all (key in data for key in ['ten','soTrang','idTacGia'])):
        ten=data['ten']
        soTrang=data['soTrang']
        idTacGia=data['idTacGia']

        # Kiểm tra tác giả tồn tại
        book=Books.query.filter_by(ten=ten).all()
        if book:
            return "Sách đã tồn tại tồn tại!"
        try:
            new_book=Books(ten=ten,soTrang=soTrang,idTacGia=idTacGia)
            db.session.add(new_book)
            db.session.commit()

            return "Thêm Sách Thành Công!"
        except Exception as e:
            db.session.rollback()   #Quay lại phiên giao dịch nếu có lỗi
            return "Lỗi: "+str(e)
    else:
        return "Thiếu thông tin cần thiết!"
    
# Hiển thị thông tin sách theo id

def get_book_by_id_services(id):
    book=Books.query.get(id)
    print(book.ten)
    
    if not book:
        return "Sách không tồn tại!"
    else:
        return book_Schema.jsonify(book)
    
# Hiển thị tất cả thông tin sách

def get_all_books_services():
    book = Books.query.all()
    
    if book:
        return books_Schema.jsonify(book)
    else:
        return "Không có sách nào!"
    
# Cập nhật thông tin sách theo id
def update_book_services(id):
    book = Books.query.get(id)
    data=request.json
    
    if book:
        try:
            if 'ten' in data:
                book.ten=data['ten']
            if 'soTrang' in data:
                book.soTrang=data['soTrang']
            if 'idTacGia' in data:
                book.idTacGia=data['idTacGia']
            db.session.commit()
            return "Cập nhật thành công!"
        except Exception as e:
            db.session.rollback()
            return "Lỗi: "+str(e)
    else:
        return "Sách không tồn tại!"
    
# Xoá thông tin sách theo id

def delete_book_by_id_services(id):
    book = Books.query.get(id)
    data = request.json
    
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return "Xoá thành công!"
        except Exception as e:
            db.session.rollback()
            return "Lỗi: "+str(e)
    else:
        return "Sách không tồn tại!"
        
# Xoá sách theo tên

def delete_book_by_name_services(ten):
    # Kiểm tra tên sách hợp lệ
    if not ten or len(ten.strip())==0:
        return "Không có sách!" ,400
    try:
        # Tìm tất cả sách có tên trùng khớp
        books = Books.query.filter_by(ten=ten).all()
        if not books:
            return "Không có sách!" ,400
        
        # Xóa tất cả sách cùng tên
        for book in books:
            db.session.delete(book)
        db.session.commit()
        
        return f"Đã xóa {len(books)} sách có tên '{ten}'!", 200
    except Exception as e:
        db.session.rollback()
        return f"Lỗi {str(e)}"
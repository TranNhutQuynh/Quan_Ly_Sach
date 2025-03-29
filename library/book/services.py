#Logic Nghiệp vụ (business logic)

from library.extension import db
from library.library_ma import BooksSchema
from library.models import Books
from flask import request, jsonify

# Khởi tạo đối tượng Schema
book_Schema = BooksSchema()      # lấy 1 quyển sách
books_Schema = BooksSchema(many=True)   # lấy nhiều quyển sách

def add_book_services():
    data = request.json
    # Yêu cầu dữ liệu bắt buộc: ten, soTrang, idTacGia (và id là tùy chọn)
    if data and all(key in data for key in ['ten', 'soTrang']):
        ten = data['ten']
        soTrang = data['soTrang']
        
        # Nếu có cung cấp id thì kiểm tra theo id, ngược lại kiểm tra theo tên
        if 'id' in data and data['id']:
            # Nếu id được cung cấp, kiểm tra xem đã tồn tại chưa
            book = Books.query.get(data['id'])
            if book:
                return "Sách đã tồn tại theo id!"
        else:
            # Kiểm tra theo tên (không phân biệt hoa thường)
            book = Books.query.filter(Books.ten.ilike(ten)).first()
            if book:
                return "Sách đã tồn tại theo tên!"
        try:
            # Nếu có id thì truyền vào, nếu không thì để DB tự động tạo
            if 'id' in data and data['id']:
                new_book = Books(id=data['id'], ten=ten, soTrang=soTrang)
            else:
                new_book = Books(ten=ten, soTrang=soTrang)
            db.session.add(new_book)
            db.session.commit()
            return "Thêm Sách Thành Công!"
        except Exception as e:
            db.session.rollback()
            return "Lỗi: " + str(e)
    else:
        return "Thiếu thông tin cần thiết!"

def get_book_by_id_services(id):
    book = Books.query.get(id)
    if not book:
        return "Sách không tồn tại!"
    else:
        return book_Schema.jsonify(book)
    
def get_book_by_name_services(ten):
    books = Books.query.filter(Books.ten.ilike(f"%{ten}%")).all()
    return books_Schema.jsonify(books)

def get_all_books_services():
    book = Books.query.all()
    if book:
        return books_Schema.jsonify(book)
    else:
        return "Không có sách nào!"

def update_book_services(id):
    book = Books.query.get(id)
    data = request.json
    if book:
        try:
            if 'ten' in data:
                book.ten = data['ten']
            if 'soTrang' in data:
                book.soTrang = data['soTrang']
            if 'idTacGia' in data:
                book.idTacGia = data['idTacGia']
            db.session.commit()
            return "Cập nhật thành công!"
        except Exception as e:
            db.session.rollback()
            return "Lỗi: " + str(e)
    else:
        return "Sách không tồn tại!"

def delete_book_by_id_services(id):
    book = Books.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return "Xoá thành công!"
        except Exception as e:
            db.session.rollback()
            return "Lỗi: " + str(e)
    else:
        return "Sách không tồn tại!"

def delete_book_by_name_services(ten):
    if not ten or len(ten.strip()) == 0:
        return "Không có sách!", 400
    try:
        # Tìm tất cả sách có tên chính xác (có thể thay đổi nếu muốn dùng tìm kiếm mờ)
        books = Books.query.filter(Books.ten == ten).all()
        if not books:
            return "Không có sách!", 400
        for book in books:
            db.session.delete(book)
            db.session.commit()
        return f"Đã xóa {len(books)} sách có tên '{ten}'!", 200
    except Exception as e:
        db.session.rollback()
        return f"Lỗi {str(e)}", 500

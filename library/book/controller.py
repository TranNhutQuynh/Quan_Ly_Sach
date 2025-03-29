from flask import Blueprint, request
from .services import (
    add_book_services,
    get_book_by_id_services,
    get_all_books_services,
    update_book_services,
    delete_book_by_id_services,
    get_book_by_name_services,
    delete_book_by_name_services
)
from flask import render_template, redirect, url_for

book_bp = Blueprint('book', __name__)

# Thêm sách (cho phép thêm theo id nếu cung cấp)
@book_bp.route("/book_management/add_book", methods=['POST'])
def add_book():
    return add_book_services()

# Xem sách theo id
@book_bp.route("/book_management/get_book/<int:id>", methods=['GET'])
def get_book_by_id(id):
    return get_book_by_id_services(id)

# Xem tất cả sách
@book_bp.route("/book_management/get_all_book", methods=['GET'])
def get_all_book():
    return get_all_books_services()

# Tìm kiếm sách theo tên
@book_bp.route("/book_management/search_book/<string:ten>", methods=['GET'])
def search_book_by_name(ten):
    return get_book_by_name_services(ten)

# Cập nhật thông tin sách theo id
@book_bp.route("/book_management/update_book/<int:id>", methods=['PUT'])
def update_book(id):
    return update_book_services(id)

# Xoá sách theo id
@book_bp.route("/book_management/delete_book/<int:id>", methods=['DELETE'])
def delete_book_by_id(id):
    return delete_book_by_id_services(id)

# Xoá sách theo tên
@book_bp.route("/book_management/delete_book/<string:ten>", methods=['DELETE'])
def delete_book_by_name(ten):
    result, status_code = delete_book_by_name_services(ten)
    return result, status_code

from library.extension import db
from library.library_ma import AccountSchema
from library.models import Account
from flask import (request, jsonify,render_template,
                   flash,redirect,url_for,session)

# Đăng Ký
def SignUp_services():
    try:
        # Lấy dữ liệu từ request: hỗ trợ cả JSON và form
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
        
        # Lấy thông tin đăng ký: username và password
        username_input = data.get('username')
        password_input = data.get('password')
        
        # Kiểm tra dữ liệu đầu vào
        if not username_input or not password_input:
            return jsonify({'message': 'Thiếu thông tin đăng ký'}), 400

        # Kiểm tra xem tài khoản đã tồn tại hay chưa
        existing_user = Account.query.filter_by(username=username_input).first()
        if existing_user:
            flash("Tài khoản đã tồn tại!")
            return render_template("signup.html", message="Tài khoản đã tồn tại!")
        
        # Tạo đối tượng Account mới (đảm bảo rằng model Account có __init__ phù hợp)
        new_user = Account(username=username_input, password=password_input)
        db.session.add(new_user)
        db.session.commit()
        
        flash("Tạo tài khoản thành công!")
        # Sau khi đăng ký thành công, chuyển hướng về trang đăng nhập (hoặc giao diện phù hợp)
        return render_template("login.html", message="Tạo tài khoản thành công!")
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error', 'error': str(e)}), 400



#  Đăng nhập

def Login_services():
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
        
        username = data.get('username')
        password = data.get('password')
        
        # Truy vấn tài khoản với thông tin đăng nhập
        account = Account.query.filter_by(username=username, password=password).first()
        
        if account:
            flash("Đăng nhập thành công!")
            return render_template("home.html",message = "Đăng nhập thành công!")
        else:
            flash("Đăng nhập thất bại!")
            return render_template("login.html",message = "Đăng nhập thất bại!")  # Nếu tài khoản tồn tại


    except Exception as e:
        return jsonify({"message": "Error", "error": str(e)}), 400

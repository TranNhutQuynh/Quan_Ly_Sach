from library.extension import db
from library.library_ma import AccountSchema
from library.models import Account
from flask import request, jsonify,render_template,flash,redirect,url_for

# Đăng Ký

def Sign_Up():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        tentk = request.form.get('username')
        matkhau = request.form.get('password')
        
        # Validate dữ liệu
        if not tentk or not matkhau:
            flash('Vui lòng điền đầy đủ thông tin', 'danger')
            return render_template('login.html')
        
        # Kiểm tra username tồn tại
        check_user=Account.query.filter_by(tentk=tentk).first()
        if check_user:
            flash('Tên tài khoản đã tồn tại', 'danger')
            return render_template('login.html')
        if not check_user:
            try:
                new_account = Account(
                    username=username,
                    password=password
                )
                db.session.add(new_account)
                db.session.commit()
                
                flash('Đăng ký thành công! Vui lòng đăng nhập', 'success')
                return redirect(url_for('home.login'))
            except Exception as e:
                db.session.rollback()
                flash(f'Lỗi hệ thống: {str(e)}', 'danger')
                return render_template('home.html')


#  Đăng nhập

def Login_services():
    try:
        data = request.json
        tenTK = Account.query.filter_by(Account.users).all()
        matKhau = Account.query.filter_by(Account.password).all()
        
        if tenTK and matKhau:
            return "Đăng nhập thành công! ",render_template("home.html")
        else:
            return "Đăng nhập thất bại! ",render_template("login.html")
    except Exception as e:
        return jsonify({"message": "Error", "error": str(e)}), 400
from library.extension import db
from library.library_ma import AccountSchema
from library.models import Account
from flask import request, jsonify,render_template

# Đăng Ký

def Sign_Up():
    if request.method == 'POST':
        tentk = request.form.get['username']
        matkhau = request.form.get['password']
        


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
from flask import Blueprint, render_template,request
from .services import Login_services,SignUp_services

account_bp = Blueprint("taikhoan", __name__)

# Đăng ký tài khoản
@account_bp.route('/',methods=['GET','POST'])
def Home():
    return render_template("home.html")

@account_bp.route("/signUp",methods=['POST','GET'])
def signUp():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        return SignUp_services()

@account_bp.route("/login",methods=['GET','POST'])
def Login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        return Login_services()

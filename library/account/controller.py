from flask import Blueprint, render_template
from .services import Login_services

account_bp = Blueprint("taikhoan", __name__,template_folder='templates')

# Đăng ký tài khoản

@account_bp.route("/signUp",methods=['POST'])
def signUp():
    

@account_bp.route("/login",methods=['POST'])
def Login():
    return Login_services()

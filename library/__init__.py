from flask import Flask,request,Blueprint
from .extension import db, ma
import os
from library.book.controller import book_bp
from library.account.controller import account_bp
from .models import Books,Account

def create_db(app):
    with app.app_context():
        # Tạo riêng từng database
        db.create_all(bind_key='library')  # Tạo database library (Books + Author)
        db.create_all(bind_key='account')  # Tạo database account (Account)
    print("Tạo CSDL Thành Công!")

def create_app(config_file="config.py"):
    app=Flask(__name__)
    app.config['SECRET_KEY'] = '1234'
    app.config.from_pyfile(config_file)
    #đăng ký cơ sở dữ liệu
    db.init_app(app)
    ma.init_app(app)
    
    #Tạo CSDL
    create_db(app)
    #đăng ký blueprint
    app.register_blueprint(book_bp)
    app.register_blueprint(account_bp)
    
    return app
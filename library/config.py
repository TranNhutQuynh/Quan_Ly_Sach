import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("KEY")

# Cấu hình nhiều database chỉ sử dụng SQLALCHEMY_BINDS
SQLALCHEMY_BINDS = {
    'library': os.environ.get("DATABASE_URL_LIBRARY"),
    'account': os.environ.get("DATABASE_URL_ACCOUNT")
}
SQLALCHEMY_TRACK_MODIFICATIONS = False
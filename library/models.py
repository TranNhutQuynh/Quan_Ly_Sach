from .extension import db

# Model cho database "account"
class Account(db.Model):
    __bind_key__ = 'account'  # Liên kết với database account
    __tablename__ = "Account"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password  # Lưu ý: Nên mã hóa mật khẩu

# Model cho database "library"
class Author(db.Model):
    __bind_key__ = 'library'  # Liên kết với database library
    __tablename__ = "Author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Books', backref='author')  # Sửa relationship

    def __init__(self, name):
        self.name = name

class Books(db.Model):
    __bind_key__ = 'library'  # Liên kết với database library
    __tablename__ = "Books"
    id = db.Column(db.Integer, primary_key=True)
    ten = db.Column(db.String(256), nullable=False)
    soTrang = db.Column(db.Integer)
    idTacGia = db.Column(db.Integer, db.ForeignKey('Author.id'))  # Sửa ForeignKey

    def __init__(self, ten, soTrang, idTacGia):
        self.ten = ten
        self.soTrang = soTrang
        self.idTacGia = idTacGia
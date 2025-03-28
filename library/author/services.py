from library.extension import db
from library.library_ma import AuthorSchema
from library.models import Author
from flask import request,jsonify

author_Schema=AuthorSchema()

def add_author_services():
    data = request.json

    if data and ('name' in data):
        name = data['name']
        try:
            new_author=Author(ten=name)
            db.session.add(new_author)
            db.session.commit()

            return "thêm tác giả thành công"
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return "Thêm thất bại!"
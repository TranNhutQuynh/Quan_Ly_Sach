from flask import Blueprint,render_template
from .services import add_author_services

author_bp=Blueprint("author",__name__)

@author_bp.route("/add_author",methods=['POST'])
def add_author():
    return add_author_services()
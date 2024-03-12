from flask import Flask, request, Blueprint
from .book.controller import books

from .extension import db

def create_app(config_file="config.py"):
    app = Flask(__name__)
    
    db.init_app(app)

    app.config.from_pyfile(config_file)
    app.register_blueprint(books)
    return app
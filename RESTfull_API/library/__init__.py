from flask import Flask, request, Blueprint
from .book.controller import books
from .model import Students, Books, Author, Category, Borrows
from .extension import db, ma

import os
def create_db(app: Flask):
    with app.app_context():
        if not os.path.exists("library/library.db"):
            db.create_all()
            print("Created DB!")

def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    app.register_blueprint(books)
    return app
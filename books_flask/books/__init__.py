from flask import Flask
from books_flask.books import config
from books_flask.books.models.book_model import db
from books_flask.books.views.book import books


def create_app():

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    app.register_blueprint(books)

    return app
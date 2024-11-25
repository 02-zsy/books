from flask import Blueprint
from books_flask.books.models.book_model import db, BookDetail, BookInfo

books = Blueprint('books', __name__)


@books.route('/books/index')
def index():
    res1 = db.session.query(BookInfo).filter().paginate(page=1, per_page=10)
    data = []
    for temp in res1:
        data.append(temp.id)
        print(temp)
    return data

from . import db

class BookDetail(db.Model):
    __tablename__ = 'book_details'

    id = db.Column(db.BigInteger, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False, index=True)
    sort_id = db.Column(db.Integer, nullable=False, index=True)
    detail_title = db.Column(db.String(50))
    detail_content = db.Column(db.String)
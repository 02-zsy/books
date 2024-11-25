# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class BookDetail(db.Model):
    __tablename__ = 'book_details'

    id = db.Column(db.BigInteger, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False, index=True)
    sort_id = db.Column(db.Integer, nullable=False, index=True)
    detail_title = db.Column(db.String(50))
    detail_content = db.Column(db.String)


class BookInfo(db.Model):
    __tablename__ = 'book_infos'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False, index=True)
    book_cate = db.Column(db.String(10))
    book_name = db.Column(db.String(25))
    image_urls = db.Column(db.String(255))
    book_author = db.Column(db.String(25))
    book_status = db.Column(db.String(10))
    book_last_update_time = db.Column(db.DateTime)
    book_newest_name = db.Column(db.String(50))
    book_newest_url = db.Column(db.Integer)
    book_desc = db.Column(db.String(350))
    image_paths = db.Column(db.String(50))

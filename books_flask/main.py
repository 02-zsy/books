from flask import Flask, jsonify
from models import db
import config

from models.books_models import BookDetail

app = Flask(__name__)
app.config.from_object(config)
app.config['JSON_AS_ASCII'] = False
db.init_app(app)

@app.route('/')
def index():
    res1 = db.session.query(BookDetail).filter(BookDetail.id <= 10).all()
    data = []
    for i in res1:
        data.append({'id': i.id, 'book_id': i.book_id, "sort_id": i.sort_id, "detail_title": i.detail_title, "detail_content": i.detail_content})

    # print(res1.id, res1.book_id, res1.sort_id)
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
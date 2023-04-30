from app import flask_app
from app import db
from app.models import Book


@flask_app.route('/')
def index():
    return 'wow! its working!'


@flask_app.route('/health')
def health():
    return 'ok'


@flask_app.route('/addbook/<title>')
def add(title):
    my_book = Book(title=title, author="Bob", price=10)
    db.session.add(my_book)
    db.session.commit()
    return "successfully added!"

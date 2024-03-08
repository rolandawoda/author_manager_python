from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from api.utils.database import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __init__(self, title, year, author_id=None):
        self.title = title
        self.year = year
        self.author_id = author_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class BookSchema(SQLAlchemySchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    title = auto_field()
    year = auto_field()
    author_id = auto_field()

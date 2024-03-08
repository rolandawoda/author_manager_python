from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.books import Book, BookSchema
from api.utils.database import db


book_routes = Blueprint("book_routes", __name__)


@book_routes.route("/", methods=["POST"])
@jwt_required()
def create_book():
    try:
        data = request.get_json()
        if data['author_id']:
            book_schema = BookSchema()
            book = book_schema.load(data)
            result = book_schema.dump(book.create())
            return response_with(resp.SUCCESS_201, value={"book": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@book_routes.route("/", methods=["GET"])
def get_book_list():
    fetched_books = Book.query.all()
    book_schema = BookSchema(many=True)
    books = book_schema.dump(fetched_books)
    return response_with(resp.SUCCESS_200, value={"books": books})


@book_routes.route("/<int:id>", methods=["GET"])
def get_book_detail(id):
    fetched_book = Book.query.get_or_404(id)
    book_schema = BookSchema()
    book = book_schema.dump(fetched_book)
    return response_with(resp.SUCCESS_200, value={"book": book})


@book_routes.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_book_detail(id):
    data = request.get_json()
    fetched_book = Book.query.get_or_404(id)
    fetched_book.title = data['title']
    fetched_book.year = data['year']
    db.session.add(fetched_book)
    db.session.commit()
    book_schema = BookSchema()
    book = book_schema.dump(fetched_book)
    return response_with(resp.SUCCESS_200, value={"book": book})


@book_routes.route('/<int:id>', methods=['PATCH'])
@jwt_required()
def modify_book_detail(id):
    data = request.get_json()
    fetched_book = Book.query.get_or_404(id)
    if data.get('title'):
        fetched_book.title = data['title']
    if data.get('year'):
        fetched_book.year = data['year']
    db.session.add(fetched_book)
    db.session.commit()
    book_schema = BookSchema()
    book = book_schema.dump(fetched_book)
    return response_with(resp.SUCCESS_200, value={"book": book})


@book_routes.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    fetched_book = Book.query.get_or_404(id)
    db.session.delete(fetched_book)
    db.session.commit()
    return response_with(resp.SUCCESS_204)

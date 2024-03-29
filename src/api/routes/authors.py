from flask import Blueprint, request, url_for, current_app
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename
import os

from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.authors import Author, AuthorSchema
from api.utils.database import db

author_routes = Blueprint("author_routes", __name__)

allowed_extensions = set(['image/jpeg', 'image/png', 'jpeg'])


def allowed_file(filetype):
    return filetype in allowed_extensions


@author_routes.route('/avatar/<int:author_id>', methods=['POST'])
@jwt_required()
def upload_author_avatar(author_id):
    try:
        file = request.files['avatar']
        print("file", file.content_type)
        fetched_author = Author.query.get_or_404(author_id)
        if file and allowed_file(file.content_type):
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                current_app.config['UPLOAD_FOLDER'], filename))
        fetched_author.avatar = url_for(
            'uploaded_file', filename=filename, _external=True)
        db.session.add(fetched_author)
        db.session.commit()
        author_schema = AuthorSchema()
        author = author_schema.dump(fetched_author)
        return response_with(resp.SUCCESS_200, value={"author": author})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@author_routes.route("/", methods=['POST'])
@jwt_required()
def create_author():
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        result = author_schema.dump(author.create())
        return response_with(resp.SUCCESS_201, value={"author": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@author_routes.route("/", methods=["GET"])
def get_author_list():
    fetched_authors = Author.query.all()
    author_schema = AuthorSchema(
        many=True, only=['first_name', 'last_name', 'id'])
    authors = author_schema.dump(fetched_authors)
    return response_with(resp.SUCCESS_200, value={"authors": authors})


@author_routes.route("/<int:author_id>", methods=["GET"])
def get_author_detail(author_id):
    fetched_author = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched_author)
    return response_with(resp.SUCCESS_200, value={"author": author})


@author_routes.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_author_detail(id):
    data = request.get_json()
    fetched_author = Author.query.get_or_404(id)
    fetched_author.first_name = data['first_name']
    fetched_author.last_name = data['last_name']
    db.session.add(fetched_author)
    db.session.commit()
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched_author)
    return response_with(resp.SUCCESS_200, value={"author": author})


@author_routes.route("/<int:id>", methods=["PATCH"])
@jwt_required()
def modify_author_detail(id):
    data = request.get_json()
    fetched_author = Author.query.get_or_404(id)
    if data.get("first_name"):
        fetched_author.first_name = data['first_name']
    if data.get("last_name"):
        fetched_author.last_name = data["last_name"]
    db.session.add(fetched_author)
    db.session.commit()
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched_author)
    return response_with(resp.SUCCESS_200, value={"author": author})


@author_routes.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_author(id):
    fetched_author = Author.query.get_or_404(id)
    db.session.delete(fetched_author)
    db.session.commit()
    return response_with(resp.SUCCESS_204)

from flask import Blueprint, jsonify, request

import data
from validators import validate_book

books_bp = Blueprint("books", __name__)


# GET /api/books  or  /api/books?author=kalam
@books_bp.route("", methods=["GET"])
def list_books():
    author = request.args.get("author")
    return jsonify(data.get_all_books(author))


# GET /api/books/1
@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = data.get_book(book_id)
    if book is None:
        return jsonify({"error": f"Book with id {book_id} not found"}), 404
    return jsonify(book)


# POST /api/books
@books_bp.route("", methods=["POST"])
def create_book():
    body = request.get_json(silent=True)
    errors = validate_book(body)
    if errors:
        return jsonify({"errors": errors}), 400

    book = data.add_book(body)
    return jsonify(book), 201


# PUT /api/books/1
@books_bp.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    body = request.get_json(silent=True)
    errors = validate_book(body)
    if errors:
        return jsonify({"errors": errors}), 400

    book = data.update_book(book_id, body)
    if book is None:
        return jsonify({"error": f"Book with id {book_id} not found"}), 404
    return jsonify(book)


# DELETE /api/books/1
@books_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    if not data.delete_book(book_id):
        return jsonify({"error": f"Book with id {book_id} not found"}), 404
    return "", 204

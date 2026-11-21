from flask import Flask, jsonify

from routes.books import books_bp


def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False

    app.register_blueprint(books_bp, url_prefix="/api/books")

    @app.route("/")
    def home():
        return jsonify({"message": "Library API is running"})

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({"error": "Method not allowed"}), 405

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)

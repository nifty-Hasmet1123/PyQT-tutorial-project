from flask import (
    jsonify
)

def init_routes(app):

    @app.route("/")
    def hello():
        return jsonify({"message": "This is the front page."})
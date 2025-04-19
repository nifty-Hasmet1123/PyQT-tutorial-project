from flask import Blueprint, jsonify

example_bp = Blueprint("example_bp", __name__, url_prefix="/api")

@example_bp.route("")
def example():
    return jsonify({
        "message": "Hello from Flask!"
    })
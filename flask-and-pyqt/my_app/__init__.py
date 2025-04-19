from my_app.routes import routes
from flask import Flask

def register_blueprint(app):
    from .blueprints import blueprints

    blueprints_list = [
        (blueprints.example_bp, None)
    ]

    for blueprint, prefix in blueprints_list:
        app.register_blueprint(blueprint, url_prefix=prefix)

    # available routes as of now
    # localhost:port/
    # localhost:port/api
    # slash /api comes from the example.py

def create_app():
    app = Flask(__name__)
    register_blueprint(app)

    # register the routes seperately using callback function
    routes.init_routes(app)

    return app


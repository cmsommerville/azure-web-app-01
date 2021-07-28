from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/<name>")
    def home(name):
        return f"<h1>Hello {name}!</h1>"

    return app

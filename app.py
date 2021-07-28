from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return f"<h1>Hello {name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)

import os

from waitress import serve
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>{'!!HelloWorld !!'*10000}<h1>"


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)

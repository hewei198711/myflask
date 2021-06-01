from flask import Flask, request, Response, make_response
from markupsafe import escape

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/")
def hello_word():
    return "我是何伟大帅逼"


@app.route("/<name>")
def hello(name):
    return f"hello, {escape(name)}"


@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

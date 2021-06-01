from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


def do_the_login():
    return "欢迎登录post"


def show_the_login_form():
    return "欢迎登录get"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

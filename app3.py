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


@app.route("/greet", defaults={"name": "programmer"})
@app.route("/greet/<name>")
def greet(name):
    return "<h1>Hello, {}!<h1>".format(name)


@app.route("/hello/hewei")
def hello1():
    name = request.args.get("name", "Flask")
    return "<h1>hello, {}!<h1>".format(name)


@app.route("/hello2", methods=["GET", "POST"])
def hello2():
    return "<h1>hello, hewei!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

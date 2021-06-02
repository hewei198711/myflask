from flask import Flask, request, redirect, url_for, abort

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.before_request
def do_something():
    print("这里的代码会在每个请求处理前执行")


@app.route("/")
def hello_word():
    return "你好，何伟"


@app.route("/hello")
def hello():
    return redirect(url_for("hello_word"))


@app.route("/index")
def index():
    abort(404)
    print("404会被打印出来吗")


if __name__ == "__main__":
    app.run()

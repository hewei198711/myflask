from flask import Flask, request, make_response

import settings

app = Flask(__name__)
app.config.from_object(settings)

colors = ["广州", "深圳", "湛江"]


@app.route("/")
def hello_word():
    print(request.host)
    return "我是何伟大神"


@app.route("/hello/<name>")
def hello(name="flask"):
    return "<h1>hello, {}".format(name)


@app.route("/goback/<int:year>")
def go_back(year):
    return "<p>Welcome to {} !</p>".format(2018 - year)


@app.route("/colors/<any(blue, white, red):color>")
def three_colors(color):
    return "<p>Love is patient and kind. Love is not jealous or boastful or proud or rude.</p>"


@app.route("/users/<any({}):user>".format(str(colors)[:]))
def three_index(user):
    print(str(colors))
    return "这里是：{}".format(user)


if __name__ == "__main__":
    app.run()

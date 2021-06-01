from flask import Flask, url_for

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/")
def index():
    return "index"


@app.route("/login")
def login():
    return "login"


@app.route("/user/<username>")
def profile(username):
    return f"{username}\'s profile"


with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", username="John Doe"))


if __name__ == "__main__":
    app.run()

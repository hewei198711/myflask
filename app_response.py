from flask import Flask, make_response, json, jsonify

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/foo")
def foo():
    response = make_response("hello, word")
    response.mimetype = "text/plain"
    return response


@app.route("/foojson")
def foo_json():
    data = {
        "name": "grey li",
        "gender": "male"
    }

    response = make_response(json.dumps(data))
    response.mimetype = "application/json"

    return response


@app.route("/foojsify")
def foo_jsonify():
    data = {
        "name": "grey li",
        "gender": "male"
    }
    return jsonify(data), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0")


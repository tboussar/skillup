from flask import Blueprint, jsonify
from flask import current_app as app


main = Blueprint("main", __name__)


@main.route("/")
def welcome():
    app.request_count += 1
    return jsonify(name="Hello words", count=app.request_count)


@main.route("/<string:word>")
def check_word(word):
    app.request_count += 1
    if app.word_store.contains(word):
        return f"{word} is word"
    else:
        return f"{word} is not a word", 404

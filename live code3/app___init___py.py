from flask import Flask
from app.word_store import WordStore


def create_app():
    app = Flask(__name__)

    from .controllers import main

    app.register_blueprint(main)
    app.word_store = WordStore()
    app.request_count = 0
    return app

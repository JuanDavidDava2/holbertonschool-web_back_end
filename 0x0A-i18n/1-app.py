#!/usr/bin/env python3
"""
0x0A. i18n
"""
from flask import Flask, render_template
from os import getenv
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """hello world"""
    return render_template("1-index.html", message="Welcome to Holberton")


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

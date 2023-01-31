#!/usr/bin/env python3
"""Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """configure available languages in our app
    """
    def __init__(self) -> None:
        """Initialize config class with available language"""
        self.LANGUAGES = ['en', 'fr']
        self.BABEL_DEFAULT_LOCALE = 'en'
        self.BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def say_hello():
    """Say hello world
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3000")

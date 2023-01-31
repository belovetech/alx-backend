#!/usr/bin/env python3
"""Force locale with URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Representation of Babel configuration
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


# @babel.localeselector
def get_locale():
    """Retrieve request locale
    """
    queries = request.query_string.decode('utf-8').split("&")
    query_obj = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))

    if 'locale' in query_obj:
        if query_obj['locale'] in Config['LANGUAGES']:
            return query_obj['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def say_hello():
    """Route handler for 4-index.html
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3030")

#!/usr/bin/python3
# Runs a Flask web application with four defined routes.
from flask import Flask, escape, abort


app = Flask('__main__')
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Defines a route with a simple response.
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    Defines a route with a simple response.
    """
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Defines a route with a URL-parameter defined response.

    Args:
        text (str): text to display.
    """
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>')
def python_is_cool(text):
    """
    Defines a route with a URL-parameter (or default) defined response.

    Args:
        text (str): text to display.
    """
    return "Python {}".format(escape(text.replace('_', ' ')))


@app.route('/number/<n>')
def number(n):
    """
    Defines a route with a integer URL-parameter (or default) defined response.

    Args:
        text (str): integer to display, must be converted from string.
    """
    try:
        n = int(n)
    except ValueError:
        abort(404)

    return "{} is an integer".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

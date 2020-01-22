#!/usr/bin/python3
# Runs a Flask web application with four defined routes.
from flask import Flask, escape, abort, render_template


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

    return "{} is a number".format(n)


@app.route('/number_template/<n>')
def number_template(n):
    """
    Defines a route with a integer URL-parameter (or default) defined template
    response.

    Args:
        text (str): integer to display, must be converted from string.
    """
    try:
        n = int(n)
    except ValueError:
        abort(404)

    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

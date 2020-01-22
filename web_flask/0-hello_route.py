#!/usr/bin/python3
"""
Module for task 0.
Runs a Flask web application with a defined route.
"""
from flask import Flask


app = Flask('__main__')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Defines a route with a simple response.
    """
    return "Hello HBNB!\n"


app.run(host='0.0.0.0', port=5000)

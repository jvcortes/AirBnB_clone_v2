#!/usr/bin/python3
"""
Module for task 0.
Runs a Flask web application with a defined route.
"""
from flask import Flask


app = Flask('__main__')


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


app.run()

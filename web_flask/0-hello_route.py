#!/usr/bin/python3
# Runs a Flask web application with a defined route.
from flask import Flask


app = Flask('__main__')
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Defines a route with a simple response.
    """
    return "Hello HBNB!"


app.run(host='0.0.0.0', port=5000)

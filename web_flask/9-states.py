#!/usr/bin/python3
# Starts a Flask web application
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask('__main__')
app.url_map.strict_slashes = False


@app.route('/states')
def states_list():
    return render_template('9-states.html',
                           states=storage.all(State).values())


@app.route('/states/<id>')
def states_by_id(id):

    value = None
    states = storage.all(State).values()

    for state in states:
        if state.id == id:
            value = state

    if value:
        return render_template('9-states.html', state=value)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


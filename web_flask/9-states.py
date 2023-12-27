#!/usr/bin/python3
"""
Module Name: web_flask/9-states.py
Description: Starts Flask web application for AirBnB clone
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """ List the states in the storage """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Display list of cities in a state according to state id """
    states = storage.all(State)

    if f"State.{id}" in states:
        target_state = states[f"State.{id}"]
        return render_template('9-states.html', states=states, id=id,
                               target_state=target_state)

    return render_template('9-states.html', id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

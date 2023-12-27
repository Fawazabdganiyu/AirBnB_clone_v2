#!/usr/bin/python3
"""
Module Name: web_flask/10-hbnb_filters.py
Description: Starts Flask web application for AirBnB clone
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    """ List the states in the storage """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda anemity: anemity.name)

    return render_template('10-hbnb_filters.html', states=sorted_states,
                           amenities=sorted_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

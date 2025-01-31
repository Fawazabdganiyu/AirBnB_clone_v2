#!/usr/bin/python3
"""
Module Name: 0-hello_route.py
Description: This module defines the start of Flask application
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbtn():
    """ Display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display “HBNB” """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Display “C” followed by the value of the `text` variable """
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ isplay “Python ”, followed by the value of the `text` variable """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ Display “n is a number” """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_n_template(n):
    """ Display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

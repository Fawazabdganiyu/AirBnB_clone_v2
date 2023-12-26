#!/usr/bin/python3
"""
Module Name: 0-hello_route.py
Description: This module defines the start of Flask application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbtn():
    """ Display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display “HBNB” """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
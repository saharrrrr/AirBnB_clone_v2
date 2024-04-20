#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask
skills_app = Flask(__name__)

@skills_app.route("/", strict_slashes=False)
def Hello_hbnb():
    """ display “Hello HBNB!”"""
    return("Hello HBNB")

@skills_app.route("/hbnb")
def hbnb():
    """ display “HBNB” """
    return("HBNB")


if __name__ == "__main__":
    skills_app.run(host="0.0.0.0")

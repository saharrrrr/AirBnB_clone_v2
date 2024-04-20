#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_hbnb():
    """ display “Hello HBNB!”"""
    return("Hello HBNB")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display “HBNB” """
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace ("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def python(text ="is cool"):
    """ display “Python ”, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

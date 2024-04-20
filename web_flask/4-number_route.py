#!/usr/bin/python3
"""script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask
from flask import abort
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
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

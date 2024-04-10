#!/usr/bin/python3

"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello_1():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def hello_2(text):
    return 'C ' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_3(text='is cool'):
    return 'Python ' + text.replace('_', ' ')

@app.route("/number/<int:n>", strict_slashes=False)
def hello_route_v4(n):
    return "{} is a number".format(n)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
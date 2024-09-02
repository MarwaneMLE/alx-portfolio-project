# In this files we will define all our views functions.

from application import app
from flask import render_template


@app.route('/') # route in flask are like endpoints
def index():
    return render_template("index.html")
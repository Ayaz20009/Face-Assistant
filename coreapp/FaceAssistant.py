from coreapp import app
from flask import request
from flask import render_template


@app.route('/')
def index():
    context = {}
    return render_template("index.html",**context)


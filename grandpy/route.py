from flask import render_template

from grandpy import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

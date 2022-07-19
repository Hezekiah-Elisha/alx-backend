#!/usr/bin/env python3
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    title = 'Welcome to holberton'
    header = 'Hello world'
    return render_template('0-index.html', title=title, header=header)



if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=7000)
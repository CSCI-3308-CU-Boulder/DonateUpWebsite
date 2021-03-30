#!/bin/env python3
from flask import Flask, render_template, current_app, flash, redirect, request, session, abort
import os

app = Flask(__name__)

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route('/')
def home():
    return render_template('home.html')

# Made with help from https://pythonspot.com/login-authentication-with-flask/

@app.route('/login', methods=['POST'])
def user_login():
    if request.form['pwd'] == 'pass' and request.form['email'] == 'user':
        session['logged_in'] = True
    else:
        flash('wrong password!')
        return home()

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)


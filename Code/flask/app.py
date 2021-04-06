#!/bin/env python3
from flask import Flask, render_template, current_app, flash, redirect, request, session, abort
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dbuser:pass@localhost:5432/donateup"
db = SQLAlchemy(app)

class userModel(db.Model):
    __tablename__ = 'users'
#
    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
#    
    def __init__(self, name, email, password):
#        self.name = name
        self.email = email
        self.password = password
#
#    def __repr__(self):


@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    if session['logged_in'] == True:
        return render_template('MyProfile.html')
    else:
        return home()

# Made with help from https://pythonspot.com/login-authentication-with-flask/

@app.route('/login', methods=['POST'])
def user_login():
    Session = sessionmaker(bind=db)
    s = Session()
    userLoginRequest = request.form['email']
    passwordLoginRequest = request.form['pwd']
    userLoginRequest = userModel.query.filter_by(email=request.form['email']).first()
    if userLoginRequest:
        session['logged_in'] = True
        return profile()
    else:
        flash('wrong password!')
        return home()

@app.route('/signup', methods=['POST'])
def user_signup():
    newUser = userModel(request.form['email'],request.form['password'])
    if request.form['pwd'] == 'pass' and request.form['email'] == 'user':
        session['logged_in'] = True
    else:
        flash('wrong password!')
        return home()

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)


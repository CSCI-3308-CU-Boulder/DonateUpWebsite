#!/bin/env python3
from flask import Flask, render_template, current_app, flash, redirect, request, session, abort, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dbuser:pass@localhost:5432/donateup"
db = SQLAlchemy(app)

class userModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

#    def __repr__(self):

ur = "from EbayPriceScrape import scrapedValue"

@app.route('/profile')
def profile():
    if session['logged_in'] == True:
        return render_template('MyProfile.html')
    else:
        return home()

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route('/')
def home():
    return render_template('DonateUp_home.html')

@app.route('/addDonation', methods=['POST'])
#placeholder for where the chrome extension will send data
def addDonation():
    return render_template('DonateUp_home.html')

# Made with help from https://pythonspot.com/login-authentication-with-flask/

@app.route("/price", methods=['POST', 'GET'])
def price():
    price = 0
    if request.method == 'POST':
        url = request.form['nm']
        print(url)
        from EbayPriceScrape import main
        price = main(url)
        return render_template('DonateUp_home.html', price = price)
    else:
      user = request.args.get('nm')
      return render_template('DonateUp_home.html', price = price)

@app.route('/login', methods=['POST'])
def user_login():
    Session = sessionmaker(bind=db)
    s = Session()
    userLoginRequest = request.form['email']
    passwordLoginRequest = request.form['pwd']
    userLoginRequest = userModel.query.filter_by(email=request.form['email'],password=request.form['pwd']).first()
    #loginRequest = userModel.query.all()
    #userLoginRequest = True
    if userLoginRequest:
        session['logged_in'] = True
        return profile()
    else:
        flash('wrong password!')
        return home()

@app.route('/signup/submit', methods=['POST'])
def user_signup():
    newEmail = request.form['email']
    newUser = request.form['name']
    newPassword = request.form['password']
    confirmNewPassword = request.form['confirmPassword']
    if newPassword != confirmNewPassword:
        flash('passwords do not match')
        return redirect(url_for('home'))
    if userModel.query.filter_by(email=newEmail):
        flash('email already has an account')
        return redirect(url_for('home'))
    else:

        newAccount = userModel(newEmail,newPassword)
        db.session.add(newAccount)
        db.session.commit()
        flash('account created!')
        return redirect(url_for('pay'))

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)

#!/bin/env python3
from flask import Flask, render_template, current_app, flash, redirect, request, session, abort, url_for, send_from_directory
import os
import requests
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dbuser:pass@localhost:5432/donateup"
db = SQLAlchemy(app)

@app.route('/favicon.ico/')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

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

class donationModel(db.Model):
    __tablename__ = 'donation_history'

    donation_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    charity_id = db.Column(db.Integer())
    amount = db.Column(db.Float())
    datetime = db.Column(db.DateTime(), default=datetime.now())

    def __init__(self, user_id, charity_id, amount):
        self.user_id = user_id
        self.charity_id = charity_id
        self.amount = amount

class charityModel(db.Model):
    __tablename__ = 'charity'

    charity_id = db.Column(db.Integer, primary_key=True)
    charity_name = db.Column(db.String())
    charity_link = db.Column(db.String())
    charity_description = db.Column(db.String())

    def __init__(self, charity_name, charity_link, charity_description):
        self.charity_name = charity_name
        self.charity_link = charity_link
        self.charity_description = charity_description

ur = "from EbayPriceScrape import scrapedValue"

@app.route('/profile')
def profile():
    if session and session['logged_in']:
        authedUser = userModel.query.filter_by(user_id=session['user']).first()
        app.logger.info(authedUser.email)
        data = {'user_id': authedUser.user_id, 'email': authedUser.email, 'name': authedUser.name}
        return render_template('DonateUp_MyProfile.html', data=data)
    else:
        return home()

@app.route('/about')
def about():
    return render_template('DonateUp_AboutUs.html')

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)
    #return render_template('%s' % page_name)

@app.route('/')
def home():
    return render_template('DonateUp_home.html')

@app.route('/donate', methods=['POST'])
#placeholder for where the chrome extension will send data
#<form action="https://www.paypal.com/donate" method="post" target="_top">
#          <nput type="hidden" name="business" value="GL4TYB2U82X66" />
#          <nput type="hidden" name="item_name" value = "St Jude!">
#          <nput type="hidden" name="currency_code" value="USD" />
#          <nput type="hidden" name="amount" id="cost" value="0"/>
def addDonation():
    URL = "https://www.paypal.com/donate/"
    business = request.form['business']
    item_name = request.form['item_name']
    currency_code = request.form['currency_code']
    amount = request.form['amount']
    app.logger.info(business)
    charity = charityModel.query.filter_by(charity_link=business).first()
    if session and session['logged_in']:
        app.logger.info('asdfasfdasfd')
        addUser = session['user']
        addCharity = charity.charity_id
        addAmount = float(amount)
        newDonation = donationModel(addUser,addCharity,addAmount)
        db.session.add(newDonation)
        db.session.commit()
        #app.logger.info('%s donation successful', amount)
        #postData = {"business": form[business],
        #            "item_name": form[item_name],
        #            "currency_code": form[currency_code],
        #            "amount": form[amount]
        #            }
        #postReq = requests.post(url = URL, data = postData)
        #app.logger.info(postReq.content)
        return redirect(URL, code=307)
    else:
        return redirect(URL, code=307)

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

# Made with help from https://pythonspot.com/login-authentication-with-flask/
@app.route('/login', methods=['POST'])
def user_login():
    #Session = sessionmaker(bind=db)
    #s = Session()
    userLoginRequest = request.form['email']
    passwordLoginRequest = request.form['pwd']
    userLoginRequest = userModel.query.filter_by(email=request.form['email'],password=request.form['pwd']).first()
    #loginRequest = userModel.query.all()
    #userLoginRequest = True
    if userLoginRequest:
        session['logged_in'] = True
        session['user'] = userLoginRequest.user_id
        app.logger.info('BAR')
        app.logger.info(session['user'])
        return profile()
    else:
        flash('wrong password!')
        return home()

@app.route('/signup/submit', methods=['POST'])
def user_signup():
    newEmail = request.form['emailField']
    newUser = request.form['nameField']
    newPassword = request.form['passwordField']
    confirmNewPassword = request.form['confirmPasswordField']
    if newPassword != confirmNewPassword:
        app.logger.info('passwords do not match')
        return redirect(url_for('home'))
    if userModel.query.filter_by(email=newEmail).first():
        app.logger.info('email already exists')
        return redirect(url_for('home'))
    else:

        newAccount = userModel(newUser,newEmail,newPassword)
        db.session.add(newAccount)
        db.session.commit()
        app.logger.info('%s created account successfully', newUser)
        return redirect(url_for('home'))

@app.route('/updateProfile', methods=['POST'])
def user_update():
    newEmail = request.form['input-email']
    newUser = request.form['input-name']
    userID = session['user']
    #newPassword = request.form['passwordField']
    #confirmNewPassword = request.form['confirmPasswordField']
    #if newPassword != confirmNewPassword:
    #    app.logger.info('passwords do not match')
    #    return redirect(url_for('home'))
    userRecord = userModel.query.filter_by(user_id=userID).first()
    if ((userRecord.email != newEmail) and (userModel.query.filter_by(email=newEmail).first())):
        app.logger.info('email already exists')
        return profile()
    else:
        userRecord.name = newUser
        userRecord.email = newEmail
        db.session.commit()
        app.logger.info('%s updated account successfully', newUser)
        return profile()

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)

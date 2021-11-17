from flask import Flask, request
import os
import BankFunctions
import simplejson
import requests
import json
import uuid
from firebase import Firebase
import datetime
# import pyrebase

os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_APP'] = 'app.py'



app = Flask(__name__)

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080)

config = {
  "apiKey": "AIzaSyCqTPcsdlnkZQzAvMrsWajGobVVAcRiKLg",
  "authDomain": "softwaretestingproj.firebaseapp.com",
  "databaseURL": "https://softwaretestingproj-default-rtdb.firebaseio.com/",
  "storageBucket": "softwaretestingproj.appspot.com"
}

firebase = Firebase(config)

db = firebase.database()

#firebase = firebase.FirebaseApplication("https://softwaretestingproj-default-rtdb.firebaseio.com/", None)

def isAuthorized(apiKey):
  all_data = db.child('data').get()
  for dat in all_data.each():
    if dat.key() == apiKey:
      return True
  return False


@app.route('/')
def index():
  return 'Please select a bank function to execute: Credit Card Payoff, Simple Savings Calculator, Credit Card Minimum Payment Calculator, Mortgage Calculator, or CD Calculator.'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/getApiKey', methods=['POST'])
def getApiKey():

  if request.method == 'POST':

    apiKey = str(uuid.uuid4())

    d = request.get_json()
    data = {
      'orgName': d['orgName'],
      'industry': d['industry'],
      'fullName': d['fullName'],
      'email': d['email'],
      'ip': request.remote_addr
    }

    db.child('data').child(apiKey).set(data)

    all_data = db.child('data').get()
    # for dat in all_data.each():
    #   print(dat.key())

    return apiKey

@app.route('/revoke', methods=['POST'])
def revoke():
  if request.method == 'POST':
    db.child("data").child(request.get_json()['apiKey']).remove()
    return 'Revoked'

@app.route('/cc_payoff', methods=['POST'])
def cc_payoff():

  if(not isAuthorized(request.headers['apiKey'])):
      return 'Not Authorized', 401

  if request.method == 'POST':

    id = uuid.uuid4()
    eventid = datetime.datetime.now().strftime('%Y%m-%d%H-%M%S')
    data = request.get_json();
    data.update({'timestamp': eventid})
    db.child('requests').child(id).set(data)

    #d = simplejson.loads(request.POST.get('data'))
    d = request.get_json()
    #print(d)
    cc_balance = d['CC Balance']
    cc_interest_rate = d['CC Interest Rate']
    months = d['Months']
    json_result = BankFunctions.cc_payoff(cc_balance, cc_interest_rate, months)


    res = json.loads(json_result);
    res.update({'timestamp': eventid})
    db.child('response').child(id).set(res)
    return json.dumps(json_result)

@app.route('/simple_savings_calc', methods=['POST'])
def simple_savings_calc():

  if(not isAuthorized(request.headers['apiKey'])):
    return 'Not Authorized', 401

  if request.method == 'POST':

    id = uuid.uuid4()
    eventid = datetime.datetime.now().strftime('%Y%m-%d%H-%M%S')
    data = request.get_json();
    data.update({'timestamp': eventid})
    db.child('requests').child(id).set(data)

    #d = simplejson.loads(request.POST.get('data'))
    d = request.get_json()
    #print(d)
    initial_deposit = d['Initial Deposit']
    monthly_contrib = d['Monthly Contribution']
    time_period = d['Time Period']
    interest_rate = d['Interest Rate']
    json_result = BankFunctions.simple_savings_calc(initial_deposit, monthly_contrib, time_period, interest_rate)

    res = json.loads(json_result);
    res.update({'timestamp': eventid})
    db.child('response').child(id).set(res)
    return json.dumps(json_result)

@app.route('/cc_min_payment_calc', methods=['POST'])
def cc_min_payment_calc():

  if(not isAuthorized(request.headers['apiKey'])):
    return 'Not Authorized', 401

  if request.method == 'POST':

    id = uuid.uuid4()
    eventid = datetime.datetime.now().strftime('%Y%m-%d%H-%M%S')
    data = request.get_json();
    data.update({'timestamp': eventid})
    db.child('requests').child(id).set(data)
    #d = simplejson.loads(request.POST.get('data'))
    d = request.get_json()
    #print(d)
    cc_balance = d['CC Balance']
    cc_interest_rate = d['CC Interest Rate']
    min_payment_percent = d['Minimum Payment Percent']
    json_result = BankFunctions.cc_min_payment_calc(cc_balance, cc_interest_rate, min_payment_percent)

    res = json.loads(json_result);
    res.update({'timestamp': eventid})
    db.child('response').child(id).set(res)
    return json.dumps(json_result)


@app.route('/mortgage_calc', methods=['POST'])
def mortgage_calc():

  if(not isAuthorized(request.headers['apiKey'])):
    return 'Not Authorized', 401

  if request.method == 'POST':

    id = uuid.uuid4()
    eventid = datetime.datetime.now().strftime('%Y%m-%d%H-%M%S')
    data = request.get_json();
    data.update({'timestamp': eventid})
    db.child('requests').child(id).set(data)
    #d = simplejson.loads(request.POST.get('data'))
    d = request.get_json()
    #print(d)
    home_price = d['Home Price']
    down_payment = d['Down Payment']
    loan_length = d['Loan Length']
    interest_rate = d['Interest Rate']
    json_result = BankFunctions.mortgage_calc(home_price, down_payment, loan_length, interest_rate)

    res = json.loads(json_result);
    res.update({'timestamp': eventid})
    db.child('response').child(id).set(res)
    return json.dumps(json_result)


@app.route('/cdCalc', methods=['POST'])
def cdCalc():

  if(not isAuthorized(request.headers['apiKey'])):
    return 'Not Authorized', 401

  if request.method == 'POST':

    id = uuid.uuid4()
    eventid = datetime.datetime.now().strftime('%Y%m-%d%H-%M%S')
    data = request.get_json();
    data.update({'timestamp': eventid})
    db.child('requests').child(id).set(data)
    #d = simplejson.loads(request.POST.get('data'))
    d = request.get_json()
    #print(d)
    init_Deposit = d['Init Deposit']
    year_Period = d['Year Period']
    interest_Rate = d['Interest Rate']
    json_result = BankFunctions.cdCalc(init_Deposit, year_Period, interest_Rate)

    res = json.loads(json_result);
    res.update({'timestamp': eventid})
    db.child('response').child(id).set(res)
    return json.dumps(json_result)
    
# @app.route('/')
# def index():
#   return 'Index Page'

# @app.route('/hello')
# def hello():
#   return 'Hello, greetings from different endpoint'

# #adding variables
# @app.route('/user/<username>')
# def show_user(username):
#   #returns the username
#   return 'Username: %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#   #returns the post, the post_id should be an int
#   return str(post_id)
  



# @app.route('/login', methods=['GET','POST'])
# def login():
#   if request.method == 'POST':
#     #check user details from db
#     login_user()
#   elif request.method == 'GET':
#     #serve login page
#     serve_login_page() 

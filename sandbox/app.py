from flask import Flask, request
import os
import BankFunctions
import simplejson
import requests

os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_APP'] = 'app.py'
app = Flask(__name__)

@app.route('/')
def index():
  return 'Please select a bank function to execute: Credit Card Payoff, Simple Savings Calculator, Credit Card Minimum Payment Calculator, Mortgage Calculator, or CD Calculator.'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/cc_payoff', methods=['POST'])
def cc_payoff():
  if request.method == 'POST':
    #d = simplejson.loads(request.POST.get('data'))
    d = request.get_json()
    #print(d)
    cc_balance = d['CC Balance']
    cc_interest_rate = d['CC Interest Rate']
    months = d['Months']
    return BankFunctions.cc_payoff(cc_balance, cc_interest_rate, months)

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

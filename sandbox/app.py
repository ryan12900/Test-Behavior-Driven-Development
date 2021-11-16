from flask import Flask
import os

os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_APP'] = 'app.py'
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'


@app.route('/')
def index():
  return 'Index Page'

@app.route('/hello')
def hello():
  return 'Hello, greetings from different endpoint'

#adding variables
@app.route('/user/<username>')
def show_user(username):
  #returns the username
  return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return str(post_id)
  

 from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    #check user details from db
    login_user()
  elif request.method == 'GET':
    #serve login page
    serve_login_page() 
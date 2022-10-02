from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World! no 2 this is a git'

@app.route('/hello')
def hello():
  return 'This is the second page!'
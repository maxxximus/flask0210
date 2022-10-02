from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World! no 4 this is new at 17.21'

@app.route('/hello')
def hello():
  return 'This is the second page!'
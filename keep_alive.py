from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hello. am here for you :) :) "

def run():
  app.run(host='0.0.0.0',port=8181)

def keep_alive():
  t= Thread(target=run)
  t.start()


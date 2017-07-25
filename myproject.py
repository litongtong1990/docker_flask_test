# -*- coding:utf-8 -*-

from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is an demo test'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

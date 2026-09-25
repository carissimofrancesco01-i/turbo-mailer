# build 474744ab61
# (auto) 3aea27
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'

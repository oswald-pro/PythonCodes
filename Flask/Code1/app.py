from flask import Flask, render_template
from functions import Database


app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")

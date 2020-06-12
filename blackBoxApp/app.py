# run with env FLASK_APP=blackBoxApp.py flask run

from flask import Flask

app = Flask(__name__)

@app.route('/')
def roll_dice():
    return "This is a game!"
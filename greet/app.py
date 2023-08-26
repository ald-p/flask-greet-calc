from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def show_welcome():
    """ Returns welcome """
    return "welcome"

@app.route('/welcome/home')
def show_welcome_home():
    """ Returns welcome home """
    return "welcome home"

@app.route('/welcome/back')
def show_welcome_back():
    """ Returns welcome back """
    return "welcome back"

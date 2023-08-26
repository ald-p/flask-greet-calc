from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Calc
@app.route('/add')
def run_add():
    """ Runs add function from operations given a & b qiery strings"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

@app.route('/sub')
def run_sub():
    """ Runs sub function from operations given a & b qiery strings"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route('/mult')
def run_mult():
    """ Runs mult function from operations given a & b qiery strings"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route('/div')
def run_div():
    """ Runs div function from operations given a & b qiery strings"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))

#Further Study
operator_funcs = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def calculate(operation):
    """ Calculate given operation in path and a & b in query string"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operator_funcs[operation](a, b)
    return str(result)
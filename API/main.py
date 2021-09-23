from flask import Flask, request  # This imports library -> flask and request


app = Flask(__name__) # It creates an instance of flask


def mult(a, b):
    return a ** b

@app.route('/')
def home():
    return "Yes , It is working"

a = 2
b = 10

@app.route('/calc', methods=['GET'])
def calc():
    return str(5)
    print(request)
    #  a = request.args.get('a')
    #  print(a)
    #  b = request.args.get('b')
    #  print(b)

@app.route('user/<string:name>/', methods=['GET', 'POST'])
def user_view(name):
    print(name)



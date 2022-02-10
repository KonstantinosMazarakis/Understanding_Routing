from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"

@app.route('/<string:id>')
def Dojo(id):
    if id == "dojo":
        return "Dojo"
    else:
        return "Sorry! No response. Try again"

@app.route('/say/<string:id>')
def fmj(id):
    if id == "flask" or id=="michael" or id=="john": 
        return f"Hi {id}"
    else:
        return "Sorry! No response. Try again"

@app.route('/repeat/<int:x>/<string:y>')
def repeat(x,y):
    if x == 35 and y == "hello" or x == 80 and y == "bye" or x == 35 and y == "dogs":
        return x * f"<h1>{y}</h1>"
    else:
        return "Sorry! No response. Try again"


if __name__ == "__main__":
    app.run(debug = True)
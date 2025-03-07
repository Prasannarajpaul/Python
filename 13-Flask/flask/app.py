from flask import Flask
'''
It creates a instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
#### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course. This should be an amazing course"

@app.route("/index")
def index():
    return "Welcome to the Index Page"


if __name__=="__main__":
    app.run(debug=True)
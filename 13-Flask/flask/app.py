from flask import Flask
'''
It creates a instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course. This should be an amazing course"


if __name__=="__main__":
    app.run()
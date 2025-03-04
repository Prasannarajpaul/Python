### Put and Delete
### Working With API's -- JSON

from flask import Flask, jsonify, request

app = Flask(__name__)

## Intialize Data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome To The Sample TO-DO List App"


if __name__=='__main__':
    app.run(debug=True)
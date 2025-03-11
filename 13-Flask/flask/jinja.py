### Building URL Dynamically
## Variable Rule
### Jinja 2 Tempalte Engine

### Jinja2 Template Engine
'''
{{ }} - expressions to print output in html
{%...%} - conditions, for loops
{#...#} - comments
'''

from flask import Flask, render_template, request
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
#### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# Variable Rule
@app.route('/success/<int:score>') # <Default Parameter will be string> -> Variable Rule
def sucess(score):
    res=""
    if score>50:
        res="PASSED"
    else:
        res="FAILED"

    return render_template('result.html', results=res)
    # return "The marks you got is "+ str(score)
    
@app.route('/successres/<int:score>') # <Default Parameter will be string> -> Variable Rule
def sucessres(score):
    res=""
    if score>50:
        res="PASSED"
    else:
        res="FAILED"
    exp = {'score': score, 'res': res}
    return render_template('result1.html', results=exp)



# If Condition
@app.route('/successif/<int:score>') # <Default Parameter will be string> -> Variable Rule
def sucess(score):
    return render_template('result2.html', results=score)

if __name__=="__main__":
    app.run(debug=True)
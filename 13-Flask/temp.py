'''
FLASK FRAME Work
(End-To-End Web Application)

WSGI -> Web Server Gateway Interface
Jinja 2 Template Engine

FLASK: Web Framework which is created with the help of Python Programming Language.

WebServer -> where we deploy our entire web application
it can be AWS EC2 and can be available in Azure App, Apache, Google GCP

Web App -> created by Flask framework

Request from users --> Web Server
Whe we send a request to an web server where our web app is deployed,
the request is to be reditected to the web app and get the response.
It can be:
/home
/API
/functionalities

Inorder redirect this and comunicate with the web app we use a protocol called WSGI

Requests --> Web Server --(WSGI)-> Web App
Response <-- Web Server <-(WSGI)-- Web App

The Flask also have an Jinja 2 Template Engine

Jinja 2 --> Web template engine
Web template engine combines an web template (any pages) with a Data Source

Web Template <-- DATA SOURCE (SQL DB, CSV Sheet, ML Model, MongoDB)

Example:
1    I want to create an Web Page and have a scenario, a upload button to uplpoad an image and it has to classify it into cat or dog
    When submiting, it interacts with one ml model (cat or dog) and send the indformation

2    When creating a Login form and the data is authenticated by a Data Source

Simply, we use the layout of the page to connect the Data Source and make an Dynamic Web app

'''
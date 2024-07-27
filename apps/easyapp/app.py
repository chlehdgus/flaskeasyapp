from flask import Flask, render_template, rul_for

app=Flask(__name__)

@app.route("/")
def index():
    return 'Hello, flaskweb hihi'

@app.route("/hello/<name>",methods=['GET'],endpoint='hello-endpoint')
def hello(name):
    return f"hello!! {name}!!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",name=name)



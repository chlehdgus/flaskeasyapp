from flask import Flask, render_template, url_for, redirect, request
#from email_validator 
app=Flask(__name__)

app.comfig["SECRET_KEY"]=b'c-7\x00\x89\xa9\x17WN\xd4\xa5\xd3\xd3\xf2\x02\x97'

@app.route("/")
def index():
    return 'Hello, flaskweb hihi'

@app.route("/hello/<name>",methods=['GET'],endpoint='hello-endpoint')
def hello(name):
    return f"hello!! {name}!!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",name=name)

##문의 폼 ##
@app.route("/contact")
def contact():
    return render_template("contact.html")

##문의 완료 폼##
@app.route("/contact_complete",methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":
        username=request.form["username"]
        email=request.form["email"]
        description=request.form["description"]
        
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")


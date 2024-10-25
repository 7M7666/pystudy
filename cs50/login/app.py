
from flask import *
from flask_session import * 
app=Flask(__name__)
app.config["SESSIION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

registerants={}

@app.route("/")
def indenx():
    return render_template("index.html",name=session.get("name"))
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        session["name"]=request.form.get("name")
        return redirect("/")
    return render_template("login.html")
@app.route("/logout")
def logout():
    session.clear
    return redirect("/")
app.run(debug=True)
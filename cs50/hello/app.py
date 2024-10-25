from flask import *

app=Flask(__name__)

@app.route("/")
def indenx():
    return render_template("index.html")
@app.route("/greet",methods=["POST"])
def greet():
    name=request.form.get("name")
    return render_template("greet.html",name=name)
app.run(debug=True)

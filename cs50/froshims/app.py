
from flask import *

app=Flask(__name__)

@app.route("/")
def indenx():
    return render_template("index.html")
@app.route("/register" methods=["POST"])
def register():
    return render_template("index.html")
app.run(debug=True)

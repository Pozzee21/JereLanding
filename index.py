
from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("layout.html")

app.run( debug= True )   
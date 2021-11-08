
from flask import Flask, redirect, render_template

app = Flask(__name__)
app.secret_key='UltraSecretKeyxD'

@app.route("/")
def hello_world():
  return render_template("home.html")


@app.route("/home")
def home():
    return render_template("layout.html")

@app.route("/home2")
def home2():
    return render_template("home2.html")


if __name__ == "__main__":
    app.run(debug=True)

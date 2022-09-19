from crypt import methods
from flask import Flask, render_template, request, flash


app = Flask(__name__)


app.secret_key = "yoyo"


@app.route("/")
@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    k = request.form['fn']
    l = request.form['ln']
    kn = k.capitalize()
    nl = l.capitalize()

    flash(f"Hello {kn} {nl}! \nGreat to see you!")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

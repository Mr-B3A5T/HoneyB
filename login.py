from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "password":
            error = "Invalid credentials. Please try again."
        else:
            return redirect(url_for("dashboard"))
    return render_template("login.html", error=error)

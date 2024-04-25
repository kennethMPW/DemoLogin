from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("login page 1.html")
    else:
        un = request.form["un"]
        pw = request.form["pw"]
        if un == None:
            return render_template("login page 1.html")
        elif un == "bob" and pw == "123":
            return "Hello " + un
        else:
            return "User not recognised!"
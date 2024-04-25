from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    user = request.args.get('user')
    un = request.args.get("un")
    pw = request.args.get("pw")
    if user == None:
        return render_template("login page 1.html")
    elif un == "bob" and pw == "123":
        return "Hello " + un
    else:
        return "User not recognised!"
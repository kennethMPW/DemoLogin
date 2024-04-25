from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    user = request.args.get('user')
    if user == None:
        return render_template("login page 1.html")
    elif un == "bob" and pw == "123":
        return "Hello " + un
    else:
        return "User not recognised!"
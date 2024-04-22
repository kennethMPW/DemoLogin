from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def home():
    user = request.args.get('user')
    if user == None:
        return render_template("login page 1.html")
    elif user=="bob":
        return "Hello " + user
    else:
        return "User not recognised!"
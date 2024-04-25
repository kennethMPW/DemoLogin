print("hello")
from flask import Flask, render_template

app = Flask(__name__)
@app.rout("/")
def home():
    user = request.ags.get('user')
    print(user)
    return render_template("login page 1.html")
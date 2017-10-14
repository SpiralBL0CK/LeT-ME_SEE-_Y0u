from flask import Flask
from flask import render_template
from LetMESEEYOu import attack

app = Flask(__name__)

@app.route("/")
def spam_ddos(worker):
    return render_template("GUI.html",worker=worker)
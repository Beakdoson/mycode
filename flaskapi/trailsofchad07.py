#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template




from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("questionpage.html")


@app.route("/home/student/mycode/flaskapi/templates")
def correct():
    return rend_template("correctanswer.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


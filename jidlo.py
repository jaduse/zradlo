#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from kantyna import lol
from datetime import datetime
from test import lol as lol2

app = Flask(__name__)
app.config["STATIC_FOLDER"] = "static"

@app.route("/", methods=["GET"])
def hello():
    a = lol()
    b = lol2()
    print(a)
    print(b)
    return render_template("home.html", dnesni_datum=datetime.today().strftime("%A %d. %m. %Y"), date=a[0], menu=a[1], date2=b[0], menu2=b[1])

@app.route("/version", methods=["GET"])
def version():
    return render_template("version.html", ver="0.0.1")

def parse_kantyna():
    pass

    #widget widgetWysiwyg clearfix


if __name__ == "__main__":
    app.run(debug=True)


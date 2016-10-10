#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from datetime import datetime


from kantyna import lol # KANTYNA
from test import lol as lol2 # CHUTPOINT
from vrtule import lol as lol3 # VRTULE

app = Flask(__name__)
app.config["STATIC_FOLDER"] = "static"

@app.route("/", methods=["GET"])
def hello():
    a = lol() or ["", ""]
    b = lol2() or ["čus", ""]
    print("CHUTPOINT\n\n\n\n\n\n\n\n\n", b)
    c = lol3() or ["", ""]
    return render_template("home.html", dnesni_datum=datetime.today().strftime("%A %d. %m. %Y"), date=a[0], menu=a[1], date2=b[0], menu2=b[1], date3=c[0], menu3=c[1])

@app.route("/version", methods=["GET"])
def version():
    return render_template("version.html", ver="0.0.1")

def parse_kantyna():
    pass

    #widget widgetWysiwyg clearfix


if __name__ == "__main__":
    app.run(debug=True)


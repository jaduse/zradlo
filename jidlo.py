#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from kantyna import lol

app = Flask(__name__)
app.config["STATIC_FOLDER"] = "static"

@app.route("/", methods=["GET"])
def hello():
    a = lol()
    print(a)
    return render_template("home.html", date=a[0], menu=a[1])

@app.route("/version", methods=["GET"])
def version():
    return render_template("version.html", ver="0.0.1")

def parse_kantyna():
    pass

    #widget widgetWysiwyg clearfix


if __name__ == "__main__":
    app.run(debug=True)


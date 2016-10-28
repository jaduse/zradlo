#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from datetime import datetime

from kantyna import result as Kantyna # KANTYNA
from chutpoint import result as Chutpoint # CHUTPOINT
from vrtule import result as Vrtule # VRTULE

app = Flask(__name__)
app.config["STATIC_FOLDER"] = "static"

@app.route("/", methods=["GET"])
def home():
    kant_date, kant_menu = Kantyna()
    chut_date, chut_menu = Chutpoint()
    vrt_date, vrt_menu = Vrtule()

    dnesni_datum = datetime.today().strftime("%A %d. %m. %Y")
    return render_template("home.html",
        dnesni_datum=dnesni_datum,
        kant_date=kant_date,
        kant_menu=kant_menu,
        chut_date=chut_date,
        chut_menu=chut_menu,
        vrt_date=vrt_date,
        vrt_menu=vrt_menu
    )

if __name__ == "__main__":
    app.run(debug=True)


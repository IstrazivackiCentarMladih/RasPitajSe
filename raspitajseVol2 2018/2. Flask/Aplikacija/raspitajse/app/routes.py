from app import raspitajse
from flask import render_template

@raspitajse.route('/')
@raspitajse.route('/index/')
def index():
    lista_bulleta = [
        "RasPitaj se!",
        "Summer of Code",
        "IYNT"
    ]
    return render_template('index.html',
                    title="moja prva flask stranica",
                    body="bok, ovo je super stranica",
                    lista=lista_bulleta)

@raspitajse.route('/green_on')
def green_on():
    return render_template("led_status.html",
                            color="green",
                            status="on"
                          )

@raspitajse.route('/green_off')
def green_off():
    return render_template("led_status.html",
                            color="green",
                            status="off"
                          )

@raspitajse.route('/red_on')
def red_on():
    return render_template("led_status.html",
                            color="red",
                            status="on"
                          )

@raspitajse.route('/red_off')
def red_off():
    return render_template("led_status.html",
                            color="red",
                            status="off"
                          )

#!/usr/bin/env python3

from flask import Flask
#TODO: import rpi3 led library -> hint: copy .py file with its implementation in the same folder as this script
#TODO: install flask by typing 'pip3 install flask' in terminal (if you didn't already...)
app = Flask(__name__)

@app.route('/red_on')
def red_on():
    # TODO: add red on implementation here
    print("red on")
    return 'ok, red on!'

@app.route('/red_off')
def red_off():
    # TODO: add red off implementation here
    print("red off")
    return 'ok, red off!'

@app.route('/green_on')
def green_on():
    # TODO: add green on implementation here
    print("green on")
    return 'ok, green on!'

@app.route('/green_off')
def green_off():
    # TODO: add green off implementation
    print("green off")
    return 'ok, green off!'

#TODO: initialize LEDs
#TODO: this app usually usually requires port 5000. Keep this in mind when dockerizing..

#TODO: find out your ip by typing
# ip a | grep "inet " | grep -v "docker" | grep -v "127.0.0.1"
# in terminal

print("my app is running!")

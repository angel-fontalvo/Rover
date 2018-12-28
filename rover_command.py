from flask import Flask
import RPi.GPIO as gpio
import time
from random import sample as sa

app = Flask(__name__)

ENA = 7
ENB = 22
EN1 = 15
EN2 = 11
EN3 = 16
EN4 = 18

tf = .1

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(ENA, gpio.OUT)
    gpio.setup(EN1, gpio.OUT)
    gpio.setup(EN2, gpio.OUT)
    gpio.setup(ENB, gpio.OUT)
    gpio.setup(EN3, gpio.OUT)
    gpio.setup(EN4, gpio.OUT)

@app.route("/forward")
def forward():
    event = "forward"
    init()
    gpio.output(ENA, gpio.HIGH)
    gpio.output(EN1, gpio.HIGH)
    gpio.output(EN2, gpio.LOW)
    
    gpio.output(ENB, gpio.HIGH)
    gpio.output(EN3, gpio.HIGH)
    gpio.output(EN4, gpio.LOW)
    time.sleep(tf)
    gpio.cleanup()
    print(event)
    return event

@app.route("/reverse")
def reverse():
    event = "reverse"
    init()
    gpio.output(ENA, gpio.HIGH)
    gpio.output(EN1, gpio.LOW)
    gpio.output(EN2, gpio.HIGH)
    
    gpio.output(ENB, gpio.HIGH)
    gpio.output(EN3, gpio.LOW)
    gpio.output(EN4, gpio.HIGH)
    time.sleep(tf)
    gpio.cleanup()
    print(event)
    return event


@app.route("/turn_left")
def turn_left():
    event = "turn_left"
    init()
    gpio.output(ENA, gpio.HIGH)
    gpio.output(EN1, gpio.HIGH)
    gpio.output(EN2, gpio.LOW)
    
    gpio.output(ENB, gpio.LOW)
    gpio.output(EN3, gpio.LOW)
    gpio.output(EN4, gpio.LOW)
    time.sleep(tf)
    gpio.cleanup()
    print(event)
    return event


@app.route("/turn_right")
def turn_right():
    event = "turn_right"
    init()
    gpio.output(ENA, gpio.LOW)
    gpio.output(EN1, gpio.LOW)
    gpio.output(EN2, gpio.LOW)
    
    gpio.output(ENB, gpio.HIGH)
    gpio.output(EN3, gpio.HIGH)
    gpio.output(EN4, gpio.LOW)
    time.sleep(tf)
    gpio.cleanup()
    print(event)
    return event

@app.route("/stop")
def stop():
    event = "stop"
    init()
    gpio.output(ENA, gpio.LOW)
    gpio.output(EN1, gpio.LOW)
    gpio.output(EN2, gpio.LOW)
    
    gpio.output(ENB, gpio.LOW)
    gpio.output(EN3, gpio.LOW)
    gpio.output(EN4, gpio.LOW)
    time.sleep(tf)
    gpio.cleanup()
    print(event)
    return event

@app.route("/status")
def status():
    return "you're good to goooo"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5004')

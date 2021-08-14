from flask import Flask, render_template,request,Response
import RPi.GPIO as GPIO
import sys
import signal
import time
import cv2
from camera import Camera

prestates="stop"

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def gen(camera):
    while True:
        frame = camera.get_frame()

        if frame is not None:
            yield (b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n")
        else:
            print("frame is none")

def tankForward(value=255):
            GPIO.output(23,True)
            GPIO.output(24,False)
            GPIO.output(22,True)
            GPIO.output(27,False)

def tankBackward(value=255):
            GPIO.output(23,False)
            GPIO.output(24,True)
            GPIO.output(22,False)
            GPIO.output(27,True)

def tankLeft(value=255):
            GPIO.output(23,True)
            GPIO.output(24,False)
            GPIO.output(22,False)
            GPIO.output(27,True)

def tankRight(value=255):
            GPIO.output(23,False)
            GPIO.output(24,True)
            GPIO.output(22,True)
            GPIO.output(27,False)

def tankStop(value=255):
            GPIO.output(23,False)
            GPIO.output(24,False)
            GPIO.output(22,False)
            GPIO.output(27,False)


@app.route("/on",methods=["POST"])
def Tank():
    if request.method == "POST":

        if "forward"==request.form['name']:
            print("-"*20)
            tankForward()
            print("Forward")
        elif "backward"==request.form['name']:
            print("-"*20)
            print("Backward")
            tankBackward()
        elif "left" == request.form['name']:
            print("-"*20)
            tankLeft()
            print("left")
        elif "right"==request.form['name']:
            print("-"*20)
            tankRight()
            print("right")
        else:
            tankStop()
            print("-"*20)
            print("STOP")
            print("-"*20)
        prestates=request.form['name']
    return render_template('index.html')

def sigint_handler(signal, frame):
    app.logger.debug("Closing")
    GPIO.cleanup()
    app.logger.debug("Closed")
    sys.exit(0)

@app.route("/video_feed")
def video_feed():
    return Response(gen(Camera()),
            mimetype="multipart/x-mixed-replace; boundary=frame")
if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)


    app.run("0.0.0.0")

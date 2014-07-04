#!/usr/bin/python

from flask import Flask, render_template,jsonify
from raspirobotboard import RaspiRobot

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/forward')
def forward():
	rr.forward(0.5)
	return jsonify(status = '0')

@app.route('/reverse')
def reverse():
	rr.reverse(0.5)
	return jsonify(status = '0')

@app.route('/left')
def left():
	rr.left(0.5)
	return jsonify(status = '0')

@app.route('/right')
def right():
	rr.right(0.5)
	return jsonify(status = '0')

@app.route('/stop')
def stop():
	rr.stop()
	return jsonify(status = '0')

# init
rr = RaspiRobot()


if __name__ == "__main__":
	app.run(host='0.0.0.0', port = 5001)

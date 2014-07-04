#!/usr/bin/python

from flask import Flask, render_template,jsonify, request
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

@app.route('/led1', methods=['POST'])
def led1():
	if request.json:
		state = 0
		try:
			state = int(request.json.get('state', 0))
		except:
			pass

		rr.set_led1(state)

	return jsonify(status = '0')


# init
rr = RaspiRobot()


if __name__ == "__main__":
	app.run(host='0.0.0.0', port = 5001, debug = True)

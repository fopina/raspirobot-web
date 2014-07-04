#!/usr/bin/python

from flask import Flask, render_template,jsonify, request, abort
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

@app.route('/output', methods=['POST'])
def switch():
	if not request.json:
		abort(400)

	switch_name = request.json.get('switch')

	if type(switch_name) is not unicode:
		abort(400)

	if switch_name not in ['led1', 'led2', 'oc1', 'oc2']:
		abort (400)

	if 'state' in request.json:
		state = request.json['state']

		if type(state) is not bool:
			abort(400)

		method = getattr(rr, 'set_' + switch_name)
		method(state)

	return jsonify(state = state)

@app.route('/output/<switch_name>', methods=['GET','POST'])
def output(switch_name):
	if switch_name not in [ 'led1', 'led2', 'oc1', 'oc2' ]:
		abort (400)

	state = False

	if request.json:
		if 'state' not in request.json:
			abort(400)

		state = request.json['state']

		if type(state) is not bool:
			abort(400)

		method = getattr(rr, 'set_' + switch_name)
		method(state)

	return jsonify(state = state)

@app.route('/input/<switch_name>', methods=['GET','POST'])
def input(switch_name):
	if switch_name not in [ 'sw1', 'sw2' ]:
		abort (400)
	
	state = getattr(rr, switch_name + '_closed')()

	return jsonify(closed = state)

# init
rr = RaspiRobot()


if __name__ == "__main__":
	app.run(host='0.0.0.0', port = 5001, debug = True)

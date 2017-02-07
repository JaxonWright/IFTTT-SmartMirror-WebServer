from flask import Flask, request, json
import os

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello world'

@app.route('/IFTTT', methods=['POST'])
def foo():
	print (request.json)
	if request.json['data'] == 'turn on':
		os.system("echo 'on 0' | cec-client -s")
		return 'turning on'
	if request.json['data'] == 'turn off':
		os.system("echo 'standby 0' | cec-client -s")
		return 'turning off'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

import flask
import subprocess
from node_vm2 import VM
import sys
import requests, json
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
app = flask.Flask('app')

@app.route('/')
def main():
	return flask.send_from_directory('public', 'index.html')
@app.route('/resources/public/static/style')
def style():
	return flask.send_from_directory('public', 'style.css')
@app.route('/resources/public/static/script')
def script():
	return flask.send_from_directory('public', 'script.js')

@app.route('/node')
def node():
	code = open("thing.js", "w")
	code.write(flask.request.args.get('code'))
	code = open("thing.js", "r")
	data = json.dumps({
		"language": "js",
  	"source": code.read()
	}, indent = 2)
	code.close()
	resp = requests.post("https://emkc.org/api/v1/piston/execute/", headers=headers, data=data)
	out = resp.json()['output']
	return flask.redirect("/embed?title=Node.js&body=Output: \n" + str(out))

@app.route('/embed')
def embed():
	return '<meta content="{0}" property="og:title"><meta content="{1}" property="og:description">'.format(flask.request.args.get('title'),flask.request.args.get('body')) 

# @app.route('/node')
# def node():
# 	arg_in = flask.request.args.get('in')
# 	arg_out = ''
# 	with VM() as vm:
# 		arg_out = vm.run('eval(() => {' + arg_in + '})')
# 		print(arg_out)
# 	return flask.redirect('https://embed.spidunno.gq/embed?title=node.js&body={0}'.format(arg_out))

app.run(host='0.0.0.0', port=8080)
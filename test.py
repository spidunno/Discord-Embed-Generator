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
	lgge = flask.request.args.get('lgge')
	data = json.dumps({
		"language": lgge,
  	"source": code.read()
	}, indent = 2)
	code.close()
	resp = requests.post("https://emkc.org/api/v1/piston/execute/", headers=headers, data=data)
	out = resp.json()['output']
	codefile = open("thing.js", "r")
	code = codefile.read()
	codefile.close()
	return """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>repl.it</title>
		<meta content="{0}" property="og:title"><meta content="{1}" property="og:description">
    <style>body {
	background-color: rgb(39, 37, 53);
}
code[class*="language-"],
pre[class*="language-"] {
	text-align: left;
	white-space: pre;
	word-spacing: normal;
	word-break: normal;
	word-wrap: normal;
	color: #eee;
	background: #2f2f2f;
	font-family: Roboto Mono, monospace;
	font-size: 1em;
	line-height: 1.5em;

	-moz-tab-size: 4;
	-o-tab-size: 4;
	tab-size: 4;

	-webkit-hyphens: none;
	-moz-hyphens: none;
	-ms-hyphens: none;
	hyphens: none;
}

code[class*="language-"]::-moz-selection,
pre[class*="language-"]::-moz-selection,
code[class*="language-"] ::-moz-selection,
pre[class*="language-"] ::-moz-selection {
	background: #363636;
}

code[class*="language-"]::selection,
pre[class*="language-"]::selection,
code[class*="language-"] ::selection,
pre[class*="language-"] ::selection {
	background: #363636;
}

:not(pre) > code[class*="language-"] {
	white-space: normal;
	border-radius: 0.2em;
	padding: 0.1em;
}

pre[class*="language-"] {
	overflow: auto;
	position: relative;
	margin: 0.5em 0;
	padding: 1.25em 1em;
}

.language-css > code,
.language-sass > code,
.language-scss > code {
	color: #fd9170;
}

[class*="language-"] .namespace {
	opacity: 0.7;
}

.token.atrule {
	color: #c792ea;
}

.token.attr-name {
	color: #ffcb6b;
}

.token.attr-value {
	color: #a5e844;
}

.token.attribute {
	color: #a5e844;
}

.token.boolean {
	color: #c792ea;
}

.token.builtin {
	color: #ffcb6b;
}

.token.cdata {
	color: #80cbc4;
}

.token.char {
	color: #80cbc4;
}

.token.class {
	color: #ffcb6b;
}

.token.class-name {
	color: #f2ff00;
}

.token.comment {
	color: #616161;
}

.token.constant {
	color: #c792ea;
}

.token.deleted {
	color: #ff6666;
}

.token.doctype {
	color: #616161;
}

.token.entity {
	color: #ff6666;
}

.token.function {
	color: #c792ea;
}

.token.hexcode {
	color: #f2ff00;
}

.token.id {
	color: #c792ea;
	font-weight: bold;
}

.token.important {
	color: #c792ea;
	font-weight: bold;
}

.token.inserted {
	color: #80cbc4;
}

.token.keyword {
	color: #c792ea;
}

.token.number {
	color: #fd9170;
}

.token.operator {
	color: #89ddff;
}

.token.prolog {
	color: #616161;
}

.token.property {
	color: #80cbc4;
}

.token.pseudo-class {
	color: #a5e844;
}

.token.pseudo-element {
	color: #a5e844;
}

.token.punctuation {
	color: #89ddff;
}

.token.regex {
	color: #f2ff00;
}

.token.selector {
	color: #ff6666;
}

.token.string {
	color: #a5e844;
}

.token.symbol {
	color: #c792ea;
}

.token.tag {
	color: #ff6666;
}

.token.unit {
	color: #fd9170;
}

.token.url {
	color: #ff6666;
}

.token.variable {
	color: #ff6666;
}

#output {
	width: calc(100% - 50px);
  height: calc(100vh - 25px);
	display: block;
  margin-left: auto;
	margin-right: auto;
	text-align: left;
	white-space: pre;
	word-spacing: normal;
	word-break: normal;
	word-wrap: normal;
	color: #eee;
	background: #2f2f2f;
	font-family: Roboto Mono, monospace;
	font-size: 1em;
	line-height: 1.5em;

	-moz-tab-size: 4;
	-o-tab-size: 4;
	tab-size: 4;

	-webkit-hyphens: none;
	-moz-hyphens: none;
	-ms-hyphens: none;
	hyphens: none;
}

code[class*="language-"]::-moz-selection,
pre[class*="language-"]::-moz-selection,
code[class*="language-"] ::-moz-selection,
pre[class*="language-"] ::-moz-selection {
	background: #363636;
}

code[class*="language-"]::selection,
pre[class*="language-"]::selection,
code[class*="language-"] ::selection,
pre[class*="language-"] ::selection {
	background: #363636;
}

:not(pre) > code[class*="language-"] {
	white-space: normal;
	border-radius: 0.2em;
	padding: 0.1em;
}

pre[class*="language-"] {
	overflow: auto;
	position: relative;
	margin: 0.5em 0;
	padding: 1.25em 1em;
}

.language-css > code,
.language-sass > code,
.language-scss > code {
	color: #fd9170;
}

[class*="language-"] .namespace {
	opacity: 0.7;
}

.token.atrule {
	color: #c792ea;
}

.token.attr-name {
	color: #ffcb6b;
}

.token.attr-value {
	color: #a5e844;
}

.token.attribute {
	color: #a5e844;
}

.token.boolean {
	color: #c792ea;
}

.token.builtin {
	color: #ffcb6b;
}

.token.cdata {
	color: #80cbc4;
}

.token.char {
	color: #80cbc4;
}

.token.class {
	color: #ffcb6b;
}

.token.class-name {
	color: #f2ff00;
}

.token.comment {
	color: #616161;
}

.token.constant {
	color: #c792ea;
}

.token.deleted {
	color: #ff6666;
}

.token.doctype {
	color: #616161;
}

.token.entity {
	color: #ff6666;
}

.token.function {
	color: #c792ea;
}

.token.hexcode {
	color: #f2ff00;
}

.token.id {
	color: #c792ea;
	font-weight: bold;
}

.token.important {
	color: #c792ea;
	font-weight: bold;
}

.token.inserted {
	color: #80cbc4;
}

.token.keyword {
	color: #c792ea;
}

.token.number {
	color: #fd9170;
}

.token.operator {
	color: #89ddff;
}

.token.prolog {
	color: #616161;
}

.token.property {
	color: #80cbc4;
}

.token.pseudo-class {
	color: #a5e844;
}

.token.pseudo-elereturn flask.redirect("/embed?title=" + flask.request.args.get('lgge') + "&body=Output: \n" + str(out))
	color: #a5e844;return flask.redirect("/embed?title=" + flask.request.args.get('lgge') + "&body=Output: \n" + str(out))
}

.token.punctuatioreturn flask.redirect("/embed?title=" + flask.request.args.get('lgge') + "&body=Output: \n" + str(out))
	color: #89ddff;return flask.redirect("/embed?title=" + flask.request.args.get('lgge') + "&body=Output: \n" + str(out))
}

.token.regex {
	color: #f2ff00;return flask.redirect("/embed?title=" + flask.request.args.get('lgge') + "&body=Output: \n" + str(out))
}

.token.selector {
	color: #ff6666;
}

.token.string {
	color: #a5e844;
}

.token.symbol {
	color: #c792ea;
}

.token.tag {
	color: #ff6666;
}

.token.unit {
	color: #fd9170;
}

.token.url {
	color: #ff6666;
}

.token.variable {
	color: #ff6666;
}
  margin-right: auto;
	margin-top: 25px;
	margin-bottom: calc(25px);
}</style>
  </head>
  <body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/prism.min.js"></script>
		<code class="language-shell-session" id="output">{2}</code>
  </body>
</html>""".replace('{0}', flask.request.args.get('lgge')).replace('{1}', "Output:\n" + str(out)).replace('{2}', "Code:\n" + code + "\nOutput:\n" + str(out)) 


# @app.route('/node')
# def node():
# 	arg_in = flask.request.args.get('in')
# 	arg_out = ''
# 	with VM() as vm:
# 		arg_out = vm.run('eval(() => {' + arg_in + '})')
# 		print(arg_out)
# 	return flask.redirect('https://embed.spidunno.gq/embed?title=node.js&body={0}'.format(arg_out))

app.run(host='0.0.0.0', port=8080)
from flask import Flask, session, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
	session['todolist'] = []
	return render_template('index.html')

@app.route('/todo/create', methods=['POST'])
def addTask():
	content = request.form['content']
	if (content == ''):
		return jsonify(result="fail", msg="no task was given")
	else:
		session['todolist'].append(content)
		session.modified = True
		return jsonify(result="success", task=content)

@app.route('/todo/read', methods=['GET'])
def fetchList():
	return jsonify(result="success", data=session['todolist'])

@app.route('/todo/update', methods=['PUT'])
def itemUpdate():
	index = int(request.form['item_count'])
	if 'todolist' in session:
		content = request.form['content']
		session['todolist'][index] = content
		session.modified = True
		return jsonify(result="success")
	return jsonify(result="fail")

@app.route('/todo/delete', methods=['DELETE'])
def itemDelete():
	index = int(request.form['item'])
	if 'todolist' in session:
		session['todolist'].pop(index)
		session.modified = True
		return jsonify(result="success")
	return jsonify(result="fail")

app.secret_key = '*\xa1\xe0\xed\x02\xa3;4\xed\xe2\xb0\xbb"\xfaPpfM\xef\xfe\xff\

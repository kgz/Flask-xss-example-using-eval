import flask
from flask import render_template, request, jsonify

app = flask.Flask(__name__)




@app.route('/', methods=['GET'])
def home():
	# return html from string
	return render_template('index.html')

@app.route('/api', methods=['GET'])
def test():
	params = request.args
	# return html from string
	name = params.get('name')
	return f'$(\'#result\').html(\'<h1>{name}</h1>\')'


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
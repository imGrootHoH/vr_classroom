import os
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')



@app.route('/room')
def index():
	return render_template('room.html')


@app.route('/teacher')
def teacher():
	return render_template('t_view.html')


@app.route('/student')
def teacher():
	return render_template('s_view.html')


if __name__ == "__main__":

	app.run(host='0.0.0.0' ,debug = True)

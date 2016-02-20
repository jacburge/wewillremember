from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/generic/')
def professional():
	return render_template('generic.html')

@app.route('/elements/')
def creative():
	return render_template('elements.html')

# @app.route('/fun/')
# def fun():
# 	return render_template('fun.html')

# @app.route('/portfolio/')
# def portfolio():
# 	return render_template('portfolio.html')

# @app.route('/boot_index/')
# def boot_index():
# 	return render_template('bootstrap_index.html')

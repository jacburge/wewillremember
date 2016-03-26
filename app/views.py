from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/story/')
def story():
	return render_template('story.html')

@app.route('/bio/')
def bio():
	return render_template('bio.html')

@app.route('/contact/')
def contact():
	return render_template('contact.html')

# @app.route('/fun/')
# def fun():
# 	return render_template('fun.html')

# @app.route('/portfolio/')
# def portfolio():
# 	return render_template('portfolio.html')

# @app.route('/boot_index/')
# def boot_index():
# 	return render_template('bootstrap_index.html')

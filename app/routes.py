from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():

	user = {"username": "martin"}
	posts = [
		{
			"author":{"username": "john"},
			"body": "Beauty lies in the eyes of the beholder"
		},
		{
			"author":{"username": "lolo"},
			"body": "life is a journey"
		},	
	]
		
	return render_template("index.html", title="Home", user=user,  posts=posts) 

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('login requested for user {}, remember me {}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('/index'))
	return render_template('login.html', title='Sign In', form=form)
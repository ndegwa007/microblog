from flask import render_template
from app import app


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
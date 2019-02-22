import os
basedir = os.path.abspath(os.basedir.path(__file__))
class Config(object):
	"""docstring for config"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'cannot decode string'
	SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False





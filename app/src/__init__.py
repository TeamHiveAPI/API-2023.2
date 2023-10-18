from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

db = SQLAlchemy()

def create_app():
	app = Flask("__name__", instance_relative_config=False)
	app.config.from_object('config.Config')

	db.init_app(app)

	with app.app_context():
		from . import routes
		from . import auth

		app.register_blueprint(auth.auth_bp) 

		db.create_all()

		return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

db = SQLAlchemy()

def create_app():
	app = Flask(
		__name__, 
		instance_relative_config=False, 
		template_folder="templates", 
		static_folder="static")
	app.config.from_object('config.Config')

	login_manager = LoginManager()
	session = Session(app)

	db.init_app(app)
	login_manager.init_app(app)

	with app.app_context():
		from . import routes
		from . import auth
		from . import models

		app.register_blueprint(auth.auth_bp)

		db.create_all()

		return app
from flask import Flask, render_template
from flaskext.mysql import MySQL

mysql = MySQL()

def create_app():
	app = Flask("__name__", instance_relative_config=False)
	app.config.from_object('config.Config')

	mysql.init_app(app)

	with app.app_context():
		from . import routes
		from . import auth

		app.register_blueprint(auth.auth_bp)

		return app
from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.controllers.restaurant_controller import restaurant_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(restaurant_bp)

    return app

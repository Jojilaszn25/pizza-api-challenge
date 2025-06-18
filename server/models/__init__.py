from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configure SQLite DB path relative to the instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../pizza.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Pizza, Restaurant, RestaurantPizza  # Import your models

    return app

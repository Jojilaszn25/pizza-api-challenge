from flask import Flask, jsonify, request
from flask_migrate import Migrate
from server.models.db import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Pizza API"}), 200

    @app.route('/restaurants')
    def get_restaurants():
        restaurants = Restaurant.query.all()
        return jsonify([{
            "id": r.id,
            "name": r.name,
            "address": r.address
        } for r in restaurants]), 200

    @app.route('/pizzas')
    def get_pizzas():
        pizzas = Pizza.query.all()
        return jsonify([{
            "id": p.id,
            "name": p.name,
            "ingredients": p.ingredients
        } for p in pizzas]), 200

    @app.route('/restaurant_pizzas', methods=['POST'])
    def add_restaurant_pizza():
        data = request.get_json()

        try:
            new_rp = RestaurantPizza(
                price=data['price'],
                restaurant_id=data['restaurant_id'],
                pizza_id=data['pizza_id']
            )
            db.session.add(new_rp)
            db.session.commit()

            pizza = Pizza.query.get(data['pizza_id'])
            return jsonify({
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }), 201

        except Exception as e:
            return jsonify({"errors": [str(e)]}), 400

    return app

from flask import Blueprint

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route("/restaurant_pizzas")
def list_rps():
    return { "message": "RestaurantPizzas coming soon..." }

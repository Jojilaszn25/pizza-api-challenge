from flask import Blueprint

pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route("/pizzas")
def list_pizzas():
    return { "message": "Pizzas coming soon..." }

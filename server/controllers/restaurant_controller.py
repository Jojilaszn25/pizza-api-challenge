from flask import Blueprint

restaurant_bp = Blueprint('restaurant_bp', __name__)

# Placeholder route to prevent import errors
@restaurant_bp.route("/restaurants")
def list_restaurants():
    return { "message": "Restaurants coming soon..." }

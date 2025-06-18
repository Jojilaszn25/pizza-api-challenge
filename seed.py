from server.models.db import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.app import create_app

app = create_app()

with app.app_context():
    print("Seeding database...")

    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    pizza1 = Pizza(name="Pepperoni", ingredients="Cheese, Tomato Sauce, Pepperoni")
    pizza2 = Pizza(name="Margherita", ingredients="Cheese, Tomato Sauce, Basil")
    pizza3 = Pizza(name="Hawaiian", ingredients="Cheese, Pineapple, Ham")

    db.session.add_all([pizza1, pizza2, pizza3])
    db.session.commit()

    rest1 = Restaurant(name="Domino's", address="123 Pizza Street")
    rest2 = Restaurant(name="Pizza Hut", address="456 Slice Ave")

    db.session.add_all([rest1, rest2])
    db.session.commit()

    rp1 = RestaurantPizza(price=12.5, pizza_id=pizza1.id, restaurant_id=rest1.id)
    rp2 = RestaurantPizza(price=9.0, pizza_id=pizza2.id, restaurant_id=rest1.id)
    rp3 = RestaurantPizza(price=11.0, pizza_id=pizza3.id, restaurant_id=rest2.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Done seeding!")

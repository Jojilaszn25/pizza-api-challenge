from server.app import create_app
from server.models.db import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    print("Seeding database...")

    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    pepperoni = Pizza(name="Pepperoni", ingredients="Cheese, Tomato Sauce, Pepperoni")
    margherita = Pizza(name="Margherita", ingredients="Cheese, Tomato Sauce, Basil")
    bbq = Pizza(name="BBQ Chicken", ingredients="Cheese, Chicken, BBQ Sauce")
    db.session.add_all([pepperoni, margherita, bbq])
    db.session.commit()

    dominos = Restaurant(name="Domino's", address="123 Pizza Street")
    pizza_hut = Restaurant(name="Pizza Hut", address="456 Slice Ave")
    db.session.add_all([dominos, pizza_hut])
    db.session.commit()

    rp1 = RestaurantPizza(price=9.99, restaurant_id=dominos.id, pizza_id=pepperoni.id)
    rp2 = RestaurantPizza(price=7.99, restaurant_id=dominos.id, pizza_id=margherita.id)
    rp3 = RestaurantPizza(price=10.99, restaurant_id=pizza_hut.id, pizza_id=bbq.id)
    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Done seeding!")

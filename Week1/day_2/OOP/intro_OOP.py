#1.
# OOP:

# Object Oriented Programming
# - More organized / modularized
# - control over datatypes / custom datatypes
# - Store information in one place
# - Grouping of properties and functions/methods

# 2:
# What is CLASS:
# Blueprint that ensures the consistent creation of instances
# 

# 3. What are...
# Attributes/properties -- What a an object instance HAS
#  -- Car:  color, make, model, engine_model, fuel_source, 
#           license_plate, manual/automatic, transmission, mileage

# Methods -- actions/function what an objects instance can DO
#  -- paint_car(color)
#  -- drive(miles)
#  -- wash_car()
#  -- fire_employees
#  -- repair()


# Quiz Challenge:

# self.store = store
# self.items.append(item)   
# def add_item(self, item, price):   
# self.items = []
# def __init__(self, store):
# class ShoppingCart:
# return self
# self.total = 0
# self.total += price


class ShoppingCart:

    def __init__(self, specific_store):
        self.total = 0
        self.store = specific_store
        self.items = []
    
    def add_item(self, thing, price):
        self.total += price
        self.items.append(thing)
        return self

    def show_cart(self):
        print(f"Store: {self.store}, total: {self.total}")
        print(f"Items: {self.items}")

sadie_shopping_cart = ShoppingCart("Safeway")
print(sadie_shopping_cart)
print(sadie_shopping_cart.store)

nate_cart = ShoppingCart("Target")
print(nate_cart)
print(nate_cart.store)

nate_cart.store = "Amazon"
nate_cart.add_item("apples", 3.00)
nate_cart.add_item("pears", 3.00)
nate_cart.add_item("broccoli", 5.00)

nate_cart.items.append("mango")
nate_cart.total += 5.0

nate_cart.show_cart()

sadie_shopping_cart.show_cart()


# nate_cart.add_item("Star Wars Figurine", 50.00)
# nate_cart.add_item("apple", 0.99)

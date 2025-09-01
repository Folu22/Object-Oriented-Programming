# Object-Oriented-Programming
📱 Smartphone & Vehicle OOP Project
Overview

This project demonstrates Object-Oriented Programming (OOP) concepts in Python through two examples:

A Smartphone class with a specialized GamingPhone subclass.

A polymorphism example with different types of vehicles that implement the same action (move()) in unique ways.

Features
Smartphone & GamingPhone

Create smartphones with attributes like brand, model, storage, and battery.

Call, charge, and display information about a device.

GamingPhone extends Smartphone with GPU support and a play_game() method.

Supports method overriding (polymorphism).

## Vehicles with Polymorphism

A base Vehicle class with a move() method.

Subclasses (Car, Plane, Boat) implement move() differently:

🚗 Car → Driving

✈️ Plane → Flying

🚤 Boat → Sailing

Example Usage
# Smartphone
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 5000)
print(phone1.info())

phone2 = GamingPhone("Asus", "ROG 7", 512, 6000, "Adreno 740")
print(phone2.play_game("PUBG"))
print(phone2.charge())

# Vehicles
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())

Sample Output
Samsung Galaxy S24 | Storage: 256GB | Battery: 5000mAh
Asus ROG 7 is playing PUBG on Adreno 740 GPU!
Asus ROG 7 supports fast charging ⚡!
🚗 Driving on the road
✈️ Flying in the sky
🚤 Sailing on water

Concepts Demonstrated

Encapsulation → Grouping attributes & methods into classes

Inheritance → GamingPhone extends Smartphone

Polymorphism → Same method (charge() or move()) behaves differently depending on the object
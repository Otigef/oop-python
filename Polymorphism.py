class Vehicle:
    def move(self):
        pass  # Base method to be overridden

class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing ⛵")

# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for vehicle in vehicles:
    vehicle.move()

# Output:
# Car is driving 🚗
# Plane is flying ✈️
# Boat is sailing ⛵